from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import AppointmentForm
from django.utils import timezone
from .models import Appointment
from datetime import datetime, date, timedelta
from django.db.models import Count
from django.db.models import Count
from CounsellorIntern.models import DailyLog_Counsellor
from CounsellorIntern.models import Psychologist
from loging.models import CustomUser
from CounsellorIntern.models import Dailylog_Counserllor_patient
from CounsellorIntern.models import DailyNotification_Counsellor
from HRDashbaord.models import JobPostedbyHR,JobAppliedbyUser
from HRDashbaord.forms import JobPostedbyHRForm,JobAppliedbyUserForm
import random
# Create your views here.
# class register(View):
#     def get(self,request):
#         return render(request,"userend/register.html")
#     def post(self,request):
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = User_register(name=name,age=age,email=email,password=password)
#         user.save()
#         return render(request,"userend/register.html")



def know_more(request):
    return render(request,"userend/know_more.html")

# class appointment(LoginRequiredMixin, View):
#     login_url = '/create/login/'
    
#     @staticmethod
#     def Check_previous_appointment(user,fname,lname):
#         previous_appointment = Appointment.objects.filter(user=user,first_name=fname,last_name=lname).first()
#         now=datetime.now()
#         current_date=now.date()
#         if previous_appointment and (previous_appointment.appointment_date - current_date).days <= 3:
#             return True
#         else:
#             return False
#     @staticmethod
#     def doctor_free_slots(doctor):
#         doctor_free_slots = DailyLog_Counsellor.objects.filter(doctor=doctor, present=True)
#         return doctor_free_slots

#     def get(self,request):
#         form = AppointmentForm()
#         return render(request,"userend/appointment.html",{"form":form})
#     def post(self,request):
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             # Get current month and year
#             now = datetime.now()
#             # current_month = now.month
#             # current_year = now.year
#             current_date = now.date()
#             # # Check if user has more than 4 appointments in current month
#             # monthly_appointments = Appointment.objects.filter(
#             #     user=request.user,
#             #     appointment_date__year=current_year,
#             #     appointment_date__month=current_month
#             # ).count()
            
#             # if monthly_appointments >= 4:
#             #     return render(request,"userend/appointment.html",{"form":form,"error_message":"You have reached the maximum limit of 4 therapy sessions per month."})
#             # elif Appointment.objects.filter(user=request.user).exists():
#             #     return render(request,"userend/appointment.html",{"form":form,"error_message":"You have already booked an appointment."})
#             # else:
#             final=form.save(commit=False)
#             final.user = request.user
#             final.date = form.cleaned_data.get("appointment_date")  # Set the date field to match appointment_date
#                     # final.save()
#             if self.Check_previous_appointment(request.user,form.cleaned_data.get("first_name"),form.cleaned_data.get("last_name")):
#                 return render(request,"userend/appointment.html",{"form":form,"error_message":"You have already booked an appointment in the past 3 days."})
#             else:
#                 if form.cleaned_data.get("appointment_date") == current_date:
#                     av=DailyLog_Counsellor.objects.filter(present=True,date=current_date).values_list("doctor",flat=True)
#                     # for el in av:
#                     if final.selected_doctor.Auth_id in av:
#                         time_slot_choices = [("09:00","09:00"),("10:00","10:00"),("11:00","11:00"),("14:00","14:00"),("15:00","15:00"),("16:00","16:00")]
#                         slot=Dailylog_Counserllor_patient.objects.filter(doctor_id=final.selected_doctor.Auth_id,date=current_date).values_list("time_slot",flat=True)
#                         if form.cleaned_data.get("time_slot") in slot:
#                             return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date.Try for other time slots or date."})
#                             # for el in slot:
#                             #     time_slot_choices.remove(el)
#                             # if time_slot_choices.find(form.cleaned_data.get("time_slot")) == -1:
#                             #     return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date."})
#                         else:
#                                 # final.time_slot = form.cleaned_data.get("time_slot")
#                                 # final.selected_doctor = el
#                             final.Assigned_doctor = final.selected_doctor
#                             final.IsPending = False
#                             final.user = request.user

#                             final.save()
#                             Dailylog_Counserllor_patient.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=current_date,time_slot=form.cleaned_data.get("time_slot"))
#                             Name=final.selected_doctor.fname+" "+final.selected_doctor.lname
#                             time_slot=form.cleaned_data.get("time_slot")
#                             info={"Name":Name,"time_slot":time_slot,"date":current_date}
#                             return render(request,"userend/appointment_success.html",info)
#                     else:
#                         return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date.Try for other time slots or date."})
#                         # If doctor is not available today, set as pending
#                         # final.IsPending = "True"
#                         # final.save()
#                         # DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=current_date,time_slot=form.cleaned_data.get("time_slot"))
#                         # return render(request,"userend/appointment_pending.html")
#             #     else:
                
            
#                 else:
#                     # ((form.cleaned_data.get("appointment_date")) - (current_date ))<=3 and form.cleaned_data.get("appointment_date")-current_date<0:
                   
#                  #push message to counsellor if will he be available on that date and time slot and wait for the response if yes then redirect to appointment_succes with the dynamic template with teh details of the apppointment
#                     if DailyNotification_Counsellor.objects.filter(doctor_id=final.selected_doctor.Auth_id,date=form.cleaned_data.get("appointment_date"),time_slot=form.cleaned_data.get("time_slot")).exists():
#                         return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date.Try for other time slots or date."})
#                     else:
#                         final.IsPending = True
#                         final.save()
#                         DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=form.cleaned_data.get("appointment_date"),time_slot=form.cleaned_data.get("time_slot"))
#                         return render(request,"userend/appointment_pending.html")
#             # else:
                
#             #     return render(request,"userend/appointment.html",{"form":form,"error_message":"You cannot book an appointment in the past."})
#         #         # For appointments more than 3 days in the future, set as pending
#         #         final.IsPending = "True"
#         #         final.save()
#         #         DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=current_date,time_slot=form.cleaned_data.get("time_slot"))
#         #         return render(request,"userend/appointment_pending.html")
#         else:
#             # Form validation failed
#             return render(request,"userend/appointment.html",{"form":form})
# <<< ADD THESE IMPORTS AT THE TOP OF YOUR views.py FILE >>>
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta
import os

def create_google_meet_link(summary, start_time, end_time, attendees_emails):
    """
    Creates a Google Calendar event with a Meet link.
    """
    try:
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '..', 'service_account.json')

        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': summary,
            'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
            'attendees': [{'email': email} for email in attendees_emails],
            'conferenceData': {
                'createRequest': {
                    'requestId': f"{start_time.isoformat()}-{random.randint(1, 100000)}",
                    'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                }
            },
        }

        # Assuming the first attendee is the counsellor, create the event on their calendar
        event = service.events().insert(calendarId=attendees_emails[0], body=event, conferenceDataVersion=1).execute()
        
        return event.get('hangoutLink')
    except Exception as e:
        print(f"Error creating Google Meet link: {e}")
        return None

# ... your existing imports and views ...class appointment(LoginRequiredMixin, View):
    # ... your existing static methods (Check_previous_appointment, etc.) are fine ...
class appointment(LoginRequiredMixin, View):
    login_url = '/create/login/'
    @staticmethod
    def Check_previous_appointment(user,fname,lname):
        previous_appointment = Appointment.objects.filter(user=user,first_name=fname,last_name=lname).first()
        now=datetime.now()
        current_date=now.date()
        if (previous_appointment.appointment_date - current_date).days <= 7 or (current_date-previous_appointment.appointment_date).days<=7:
            return True
        else:
         return False
    @staticmethod
    def doctor_free_slots(doctor):
        doctor_free_slots = DailyLog_Counsellor.objects.filter(doctor=doctor, present=True)
        return doctor_free_slots    
   
    def get(self, request):
        # ... no changes here ...
        form = AppointmentForm()
        return render(request, "userend/appointment.html", {"form": form})

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            current_date = now.date()
            appointment_date = form.cleaned_data.get("appointment_date")
            
            # Check for past date selection
            if appointment_date < current_date:
                return render(request, "userend/appointment.html", {"form": form, "error_message": "You cannot book an appointment for a past date. Please select today or a future date."})
            
            # Check for date too far in future (more than 3 days)
            max_future_date = current_date + timedelta(days=3)
            if appointment_date > max_future_date:
                return render(request, "userend/appointment.html", {"form": form, "error_message": "You can only book appointments up to 3 days in advance. Please select a date within the next 3 days."})
            
            final = form.save(commit=False)
            final.user = request.user
            final.date = appointment_date

            if self.Check_previous_appointment(request.user, form.cleaned_data.get("first_name"), form.cleaned_data.get("last_name")):
                return render(request, "userend/appointment.html", {"form": form, "error_message": "You have already booked an appointment in the past 7 days."})
            
            # This is the main success block we will modify
            if form.cleaned_data.get("appointment_date") == current_date:
                av = DailyLog_Counsellor.objects.filter(present=True, date=current_date).values_list("doctor", flat=True)
                if final.selected_doctor.Auth_id in av:
                    slot = Dailylog_Counserllor_patient.objects.filter(doctor_id=final.selected_doctor.Auth_id, date=current_date).values_list("time_slot", flat=True)
                    
                    if form.cleaned_data.get("time_slot") in slot:
                        return render(request, "userend/appointment.html", {"form": form, "error_message": "This doctor is not available on this date. Try for other time slots or date."})
                    else:
                        final.Assigned_doctor = final.selected_doctor
                        final.IsPending = False
                        
                        # <<< START MODIFICATION: GENERATE MEET LINK >>>
                        
                        # 1. Prepare data for the helper function
                        appointment_date = current_date
                        time_slot_str = form.cleaned_data.get("time_slot")
                        appointment_time = datetime.strptime(time_slot_str, "%H:%M").time()
                        
                        start_datetime = datetime.combine(appointment_date, appointment_time)
                        end_datetime = start_datetime + timedelta(minutes=50) # Assuming a 50-minute session

                        # Get counsellor and patient emails
                        counsellor_email = final.selected_doctor.user.email # ASSUMING Psychologist model has a ForeignKey to CustomUser named 'user'
                        patient_email = request.user.email
                        attendees = [counsellor_email, patient_email]
                        
                        # 2. Call the helper function
                        meet_link = create_google_meet_link(
                            summary=f"Therapy Session for {final.first_name}",
                            start_time=start_datetime,
                            end_time=end_datetime,
                            attendees_emails=attendees
                        )

                        # 3. Save the link to the appointment object
                        final.meet_link = meet_link
                        final.save() # Now we save the final object with the meet link

                        # <<< END MODIFICATION >>>

                        Dailylog_Counserllor_patient.objects.create(doctor_id=final.selected_doctor.Auth_id, patient_id=final, date=current_date, time_slot=form.cleaned_data.get("time_slot"),meeting_link=meet_link)
                        
                        Name = final.selected_doctor.fname + " " + final.selected_doctor.lname
                        time_slot = form.cleaned_data.get("time_slot")
                        
                        # Pass the meet_link to the success template
                        info = {"Name": Name, "time_slot": time_slot, "date": current_date, "meet_link": meet_link}
                        return render(request, "userend/appointment_success.html", info)

                else:
                    return render(request, "userend/appointment.html", {"form": form, "error_message": "This doctor is on leave on this date. Try for other time slots or date."})
            
            else: # This is the logic for future (pending) appointments
                if DailyNotification_Counsellor.objects.filter(doctor_id=final.selected_doctor.Auth_id, date=form.cleaned_data.get("appointment_date"), time_slot=form.cleaned_data.get("time_slot")).exists():
                    return render(request, "userend/appointment.html", {"form": form, "error_message": "This doctor is not available on this date. Try for other time slots or date."})
                else:
                    final.IsPending = True
                    final.save()
                    DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id, patient_id=final, date=form.cleaned_data.get("appointment_date"), time_slot=form.cleaned_data.get("time_slot"))
                    
                    # NOTE: For pending appointments, you should generate the Meet link
                    # in the view where the counsellor ACCEPTS the appointment, not here.
                    
                    return render(request, "userend/appointment_pending.html")
        else:
            return render(request, "userend/appointment.html", {"form": form})

# class login(View):
#     def get(self,request):
#         return render(request,"userend/login.html")
#     def post(self,request):
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = User_login(email=email,password=password)
#         user.save()        # if user:
#         #     return redirect("userend:index")
#         # else:
#         #     return render(request,"userend/login.html")
#         return render(request,"userend/login.html")

def index(request):
    return render(request,"userend/index.html")

@login_required(login_url='/create/login/')
def appointment_success(request):
    return render(request,"userend/appointment_success.html")

@login_required(login_url='/create/login/')
def pending_approval(request):
    # Get pending appointments for the current doctor
    pending_appointments = Appointment.objects.filter(
        IsPending=True,
        selected_doctor=request.user.id
    ).order_by('appointment_date', 'time_slot')
    
    pending_count = pending_appointments.count()
    
    context = {
        'pending_appointments': pending_appointments,
        'pending_count': pending_count
    }
    
    return render(request, "userend/pending_approval.html", context)

@login_required(login_url='/create/login/')
def approve_appointment(request, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(
                id=appointment_id,
                selected_doctor=request.user.id,
                IsPending=True
            )
            
            # Update appointment status
            appointment.IsPending = False
            appointment.Assigned_doctor = appointment.selected_doctor
            appointment.save()
            
            # Create entry in Dailylog_Counserllor_patient
            from CounsellorIntern.models import Dailylog_Counserllor_patient
            Dailylog_Counserllor_patient.objects.create(
                doctor_id=appointment.selected_doctor,
                patient_id=appointment,
                date=appointment.appointment_date,
                time_slot=appointment.time_slot
            )
            
            # Redirect back to pending approvals with success message
            return redirect('userend:pending_approval')
            
        except Appointment.DoesNotExist:
            # Handle case where appointment doesn't exist or doesn't belong to this doctor
            return redirect('userend:pending_approval')
    
    return redirect('userend:pending_approval')

@login_required(login_url='/create/login/')
def reject_appointment(request, appointment_id):
    if request.method == 'POST':
        try:
            appointment = Appointment.objects.get(
                id=appointment_id,
                selected_doctor=request.user.id,
                IsPending=True
            )
            
            # Delete the appointment
            appointment.delete()
            
            # Redirect back to pending approvals
            return redirect('userend:pending_approval')
            
        except Appointment.DoesNotExist:
            # Handle case where appointment doesn't exist or doesn't belong to this doctor
            return redirect('userend:pending_approval')
    
    return redirect('userend:pending_approval')

# class counsellor(View):
#     def get(self,request):
#         return render(request,"userend/dashboard.html")
# class intern(View):
#     def get(self,request):
#         return render(request,"userend/genz_dashboard.html")

from django.http import JsonResponse
from google_calendar import create_google_meet_event

# views.py
from django.http import JsonResponse
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import datetime

# Scope to access Google Calendar with Meet links
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path to store OAuth tokens
TOKEN_PATH = 'token.json'
CREDENTIALS_PATH = 'credentials.json'  # Your downloaded OAuth credentials

def get_google_calendar_service():
    creds = None

    # If token.json exists, load it (no popup needed)
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    
    # If no valid creds, run OAuth flow (first time only)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)  # Opens consent popup once
        # Save credentials for future use
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())

    # Build Google Calendar API service
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_google_meet_event():
    service = get_google_calendar_service()

    # Set meeting start and end time (here 30 min duration)
    start_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)
    end_time = start_time + datetime.timedelta(minutes=30)

    event = {
        'summary': 'Counselling Session',
        'description': 'Online counselling appointment.',
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'randomstring1234'  # unique ID per request
            }
        },
    }

    created_event = service.events().insert(
        calendarId='primary',
        body=event,
        conferenceDataVersion=1
    ).execute()

    return created_event.get('hangoutLink')

# Django view
def create_meet_link(request):
    try:
        meet_url = create_google_meet_event()
        return JsonResponse({'meet_link': meet_url})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def open_internship(request, pk):
    """Function view to open job application form (legacy support)"""
    job = JobPostedbyHR.objects.get(id=pk)
    form = JobAppliedbyUserForm()
    return render(request, "userend/inputjobdetails.html", {"form": form, "job": job})

class internship(View):
    def get(self, request):
        today_date = timezone.now().date()
        # Get all active job postings (where last_date_to_apply hasn't passed)
        jobs = JobPostedbyHR.objects.filter(last_date_to_apply__gte=today_date).order_by('-job_posted_date')
        
        return render(request, "userend/internship.html", {"jobs": jobs})

class ApplyJob(View):
    """View to handle job application"""
    def get(self, request, pk):
        job = JobPostedbyHR.objects.get(id=pk)
        form = JobAppliedbyUserForm()
        return render(request, "userend/inputjobdetails.html", {"form": form, "job": job})
    
    def post(self, request, pk):
        job = JobPostedbyHR.objects.get(id=pk)
        form = JobAppliedbyUserForm(request.POST, request.FILES)
        
        if form.is_valid():
            application = form.save(commit=False)
            application.job_id = job
            application.save()
            
            return render(request, "userend/internship_success.html", {
                'application_id': application.id,
                'submitted_date': application.applied_date.strftime('%B %d, %Y'),
                'job_title': job.job_title
            })
        
        return render(request, "userend/inputjobdetails.html", {"form": form, "job": job})