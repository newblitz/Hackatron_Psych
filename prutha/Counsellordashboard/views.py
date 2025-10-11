from django.shortcuts import render,redirect
from django.views import View
from django.utils import timezone
from CounsellorIntern.forms import DailyLog_CounsellorFormpopup
from CounsellorIntern.models import DailyLog_Counsellor,DailyNotification_Counsellor
from .forms import DailyNotification_CounsellorForm
from userend.models import Appointment
from loging.email_service import email_service
from datetime import datetime, timedelta
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
# Create your views here.

def create_google_meet_link(summary, start_time, end_time, attendees_emails):
    """
    Creates a Google Calendar event with a GENUINE Google Meet link.
    Only returns genuine meet links - no fallbacks or fake links.
    """
    try:
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', 'service_account.json')

        # Check if service account file exists
        if not os.path.exists(SERVICE_ACCOUNT_FILE):
            print("❌ Google Calendar API: Service account file not found")
            print("📝 Please set up Google Calendar API credentials")
            return None

        print("✅ Google Calendar API: Service account file found")
        
        # Check if the service account file has valid credentials
        with open(SERVICE_ACCOUNT_FILE, 'r') as f:
            content = f.read()
            if 'your-project-id' in content or 'YOUR_PRIVATE_KEY_HERE' in content:
                print("❌ Google Calendar API: Service account file contains placeholder values")
                print("📝 Please replace with actual Google Calendar API credentials")
                return None

        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('calendar', 'v3', credentials=creds)

        # Create calendar event with conference data for GENUINE meet link
        event = {
            'summary': summary,
            'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'conferenceData': {
                'createRequest': {
                    'requestId': f"meet-{start_time.strftime('%Y%m%d%H%M%S')}",
                    'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                }
            },
        }

        # Create event with conference data to get GENUINE meet link
        event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
        meet_link = event.get('conferenceData', {}).get('entryPoints', [{}])[0].get('uri')
        
        if meet_link:
            print(f"✅ GENUINE GOOGLE MEET LINK GENERATED: {meet_link}")
            return meet_link
        else:
            print("❌ No genuine meet link generated from Google Calendar API")
            print("📝 This indicates Google Meet API is not properly configured")
            return None
        
    except Exception as e:
        print(f"❌ Google Calendar API Error: {e}")
        print("📝 Cannot generate genuine meet link - API configuration issue")
        return None

# Removed fallback functions - only genuine Google Meet links are allowed

class Notification_approval(View):
    def get(self, request):
        # Check if user is authenticated and is a counsellor
        if not request.user.is_authenticated:
            return redirect('loging:login')
        
        if request.user.user_type != 'Counsellor':
            # Redirect non-counsellors to appropriate dashboard
            if request.user.user_type == 'Patient':
                return redirect('userend:appointment')
            else:
                return redirect('loging:login')
        
        current_date=timezone.now().date()
        
        # Get pending appointments for this doctor
        pending_appointments = Appointment.objects.filter(
            selected_doctor__Auth_id=request.user,
            IsPending=True
        ).order_by('appointment_date')
        
        return render(request, "Counsellordashborad/pending_approval.html", {
            "pending_appointments": pending_appointments
        })
    def post(self, request):
        appointment_id = request.POST.get("appointment_id")
        action = request.POST.get("action")
        
        if appointment_id and action:
            try:
                appointment = Appointment.objects.get(
                    id=appointment_id,
                    selected_doctor__Auth_id=request.user,
                    IsPending=True
                )
                
                if action == "approve":
                    appointment.IsPending = False
                    appointment.Assigned_doctor = appointment.selected_doctor
                    
                    # Generate Google Meet link
                    try:
                        # Prepare data for meet link generation
                        appointment_date = appointment.appointment_date
                        time_slot_str = appointment.time_slot
                        appointment_time = datetime.strptime(time_slot_str, "%H:%M").time()
                        
                        start_datetime = datetime.combine(appointment_date, appointment_time)
                        end_datetime = start_datetime + timedelta(minutes=50)  # Assuming a 50-minute session

                        # Get counsellor and patient emails
                        counsellor_email = appointment.selected_doctor.Auth_id.email
                        patient_email = appointment.user.email
                        attendees = [counsellor_email, patient_email]
                        
                        # Generate meet link
                        meet_link = create_google_meet_link(
                            summary=f"Therapy Session for {appointment.first_name} {appointment.last_name}",
                            start_time=start_datetime,
                            end_time=end_datetime,
                            attendees_emails=attendees
                        )
                        
                        # Only accept genuine Google Meet links
                        if meet_link:
                            appointment.meet_link = meet_link
                            appointment.meet_link_type = 'genuine'
                            appointment.save()
                            
                            print(f"✅ GENUINE GOOGLE MEET LINK GENERATED: {meet_link}")
                            print(f"📊 Meet Link Type: GENUINE")
                        else:
                            print("❌ Failed to generate genuine Google Meet link")
                            print("❌ Cannot proceed without genuine meet link")
                            raise Exception("Genuine Google Meet link generation failed")
                        
                        # Send email to patient with meet link
                        patient_name = f"{appointment.first_name} {appointment.last_name}"
                        counsellor_name = f"{appointment.selected_doctor.fname} {appointment.selected_doctor.lname}"
                        
                        email_service.send_meet_link_email(
                            to_email=patient_email,
                            patient_name=patient_name,
                            counsellor_name=counsellor_name,
                            appointment_date=appointment_date.strftime('%B %d, %Y'),
                            appointment_time=time_slot_str,
                            meet_link=meet_link
                        )
                        
                        print(f"✅ Meet link generated and email sent for appointment {appointment.id}")
                        
                    except Exception as e:
                        print(f"❌ Error generating genuine Google Meet link: {e}")
                        print("❌ Cannot proceed without genuine Google Meet link")
                        print("📝 Please check Google Calendar API configuration")
                        # Don't save the appointment if we can't generate a genuine meet link
                        return redirect('Counsellordashboard:pending_approval')
                    
                    # Create entry in Dailylog_Counserllor_patient
                    from CounsellorIntern.models import Dailylog_Counserllor_patient
                    Dailylog_Counserllor_patient.objects.create(
                        doctor_id=appointment.selected_doctor.Auth_id,
                        patient_id=appointment,
                        date=appointment.appointment_date,
                        time_slot=appointment.time_slot
                    )
                    
                elif action == "reject":
                    appointment.delete()
                    
            except Appointment.DoesNotExist:
                pass  # Appointment not found or doesn't belong to this doctor
        
        return redirect('Counsellordashboard:pending_approval')

                       