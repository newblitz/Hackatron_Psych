from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import AppointmentForm
from django.utils import timezone
from .models import Appointment
from datetime import datetime, date
from django.db.models import Count
from datetime import datetime, date
from django.db.models import Count
from CounsellorIntern.models import DailyLog_Counsellor
from CounsellorIntern.models import Psychologist
from loging.models import CustomUser
from CounsellorIntern.models import Dailylog_Counserllor_patient
from CounsellorIntern.models import DailyNotification_Counsellor
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

class appointment(LoginRequiredMixin, View):
    login_url = '/create/login/'
    
    @staticmethod
    def Check_previous_appointment(user,fname,lname):
        previous_appointment = Appointment.objects.filter(user=user,first_name=fname,last_name=lname).first()
        now=datetime.now()
        current_date=now.date()
        if previous_appointment and (previous_appointment.appointment_date - current_date).days <= 3:
            return True
        else:
            return False
    @staticmethod
    def doctor_free_slots(doctor):
        doctor_free_slots = DailyLog_Counsellor.objects.filter(doctor=doctor, present=True)
        return doctor_free_slots

    def get(self,request):
        form = AppointmentForm()
        return render(request,"userend/appointment.html",{"form":form})
    def post(self,request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Get current month and year
            now = datetime.now()
            # current_month = now.month
            # current_year = now.year
            current_date = now.date()
            # # Check if user has more than 4 appointments in current month
            # monthly_appointments = Appointment.objects.filter(
            #     user=request.user,
            #     appointment_date__year=current_year,
            #     appointment_date__month=current_month
            # ).count()
            
            # if monthly_appointments >= 4:
            #     return render(request,"userend/appointment.html",{"form":form,"error_message":"You have reached the maximum limit of 4 therapy sessions per month."})
            # elif Appointment.objects.filter(user=request.user).exists():
            #     return render(request,"userend/appointment.html",{"form":form,"error_message":"You have already booked an appointment."})
            # else:
            final=form.save(commit=False)
            final.user = request.user
            final.date = form.cleaned_data.get("appointment_date")  # Set the date field to match appointment_date
                    # final.save()
            if self.Check_previous_appointment(request.user,form.cleaned_data.get("first_name"),form.cleaned_data.get("last_name")):
                return render(request,"userend/appointment.html",{"form":form,"error_message":"You have already booked an appointment in the past 3 days."})
            else:
                if form.cleaned_data.get("appointment_date") == current_date:
                    av=DailyLog_Counsellor.objects.filter(present=True,date=current_date).values_list("doctor",flat=True)
                    # for el in av:
                    if final.selected_doctor.Auth_id in av:
                        time_slot_choices = [("09:00","09:00"),("10:00","10:00"),("11:00","11:00"),("14:00","14:00"),("15:00","15:00"),("16:00","16:00")]
                        slot=Dailylog_Counserllor_patient.objects.filter(doctor_id=final.selected_doctor.Auth_id,date=current_date).values_list("time_slot",flat=True)
                        if form.cleaned_data.get("time_slot") in slot:
                            return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date.Try for other time slots or date."})
                            # for el in slot:
                            #     time_slot_choices.remove(el)
                            # if time_slot_choices.find(form.cleaned_data.get("time_slot")) == -1:
                            #     return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date."})
                        else:
                                # final.time_slot = form.cleaned_data.get("time_slot")
                                # final.selected_doctor = el
                            final.Assigned_doctor = final.selected_doctor
                            final.IsPending = False
                            final.user = request.user

                            final.save()
                            Dailylog_Counserllor_patient.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=current_date,time_slot=form.cleaned_data.get("time_slot"))
                            Name=final.selected_doctor.fname+" "+final.selected_doctor.lname
                            time_slot=form.cleaned_data.get("time_slot")
                            info={"Name":Name,"time_slot":time_slot,"date":current_date}
                            return render(request,"userend/appointment_success.html",info)
                    else:
                        return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date.Try for other time slots or date."})
                        # If doctor is not available today, set as pending
                        # final.IsPending = "True"
                        # final.save()
                        # DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=current_date,time_slot=form.cleaned_data.get("time_slot"))
                        # return render(request,"userend/appointment_pending.html")
            #     else:
                
            
                else:
                    # ((form.cleaned_data.get("appointment_date")) - (current_date ))<=3 and form.cleaned_data.get("appointment_date")-current_date<0:
                   
                 #push message to counsellor if will he be available on that date and time slot and wait for the response if yes then redirect to appointment_succes with the dynamic template with teh details of the apppointment
                    if DailyNotification_Counsellor.objects.filter(doctor_id=final.selected_doctor.Auth_id,date=form.cleaned_data.get("appointment_date"),time_slot=form.cleaned_data.get("time_slot")).exists():
                        return render(request,"userend/appointment.html",{"form":form,"error_message":"This doctor is not available on this date.Try for other time slots or date."})
                    else:
                        final.IsPending = True
                        final.save()
                        DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=form.cleaned_data.get("appointment_date"),time_slot=form.cleaned_data.get("time_slot"))
                        return render(request,"userend/appointment_pending.html")
            # else:
                
            #     return render(request,"userend/appointment.html",{"form":form,"error_message":"You cannot book an appointment in the past."})
        #         # For appointments more than 3 days in the future, set as pending
        #         final.IsPending = "True"
        #         final.save()
        #         DailyNotification_Counsellor.objects.create(doctor_id=final.selected_doctor.Auth_id,patient_id=final,date=current_date,time_slot=form.cleaned_data.get("time_slot"))
        #         return render(request,"userend/appointment_pending.html")
        else:
            # Form validation failed
            return render(request,"userend/appointment.html",{"form":form})


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

