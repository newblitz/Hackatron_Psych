from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import IntegrityError
from .forms import EmailForm, CompleteRegistrationForm, OTPVerificationForm
from .models import CustomUser, EmailVerification
from .email_service import email_service
from CounsellorIntern.models import DailyLog_Counsellor
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

# Create your views here.
class CreateAccount(View):
    """First step: Email verification"""
    
    @staticmethod
    def generate_otp():
        return random.randint(100000, 999999)

    @staticmethod
    def send_verification_email(email, otp):
        """Send verification email using SendGrid"""
        return email_service.send_verification_email(email, otp)

    def get(self, request):
        form = EmailForm()
        return render(request, "loging/registerwith.html", {"form": form})
    
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = self.generate_otp()
            
            # Delete any existing verification for this email
            EmailVerification.objects.filter(email=email).delete()
            
            # Create new verification record
            verification = EmailVerification.objects.create(
                email=email,
                otp=str(otp)
            )
            
            # Send OTP email
            print(f"DEBUG: Attempting to send OTP {otp} to {email}")
            email_sent = self.send_verification_email(email, otp)
            print(f"DEBUG: Email sending result: {email_sent}")
            
            if email_sent:
                messages.success(request, f'Verification code sent to {email}')
                # Store email in session for next step
                request.session['registration_email'] = email
                return redirect('loging:verify_otp')
            else:
                messages.error(request, 'Failed to send verification email. Please try again.')
                return render(request, "loging/registerwith.html", {"form": form})
        else:
            # Display form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return render(request, "loging/registerwith.html", {"form": form})


class VerifyOTP(View):
    """Second step: OTP verification"""
    
    def get(self, request):
        email = request.session.get('registration_email')
        if not email:
            messages.error(request, 'Please start the registration process again.')
            return redirect('loging:CreateAccount')
        
        form = OTPVerificationForm()
        return render(request, "loging/otp_verification.html", {"form": form, "email": email})
    
    def post(self, request):
        email = request.session.get('registration_email')
        if not email:
            messages.error(request, 'Please start the registration process again.')
            return redirect('loging:CreateAccount')
        
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            
            try:
                verification = EmailVerification.objects.get(email=email, otp=otp)
                
                # Check if OTP is not expired (5 minutes)
                if timezone.now() - verification.created_at > timedelta(minutes=5):
                    messages.error(request, 'OTP has expired. Please request a new one.')
                    return redirect('loging:CreateAccount')
                
                # Check attempts
                if verification.attempts >= 3:
                    messages.error(request, 'Too many failed attempts. Please start registration again.')
                    verification.delete()
                    return redirect('loging:CreateAccount')
                
                # Mark as verified
                verification.is_verified = True
                verification.save()
                
                messages.success(request, 'Email verified successfully!')
                return redirect('loging:complete_registration')
                
            except EmailVerification.DoesNotExist:
                # Increment attempts
                try:
                    verification = EmailVerification.objects.get(email=email)
                    verification.attempts += 1
                    verification.save()
                    
                    if verification.attempts >= 3:
                        messages.error(request, 'Too many failed attempts. Please start registration again.')
                        verification.delete()
                        return redirect('loging:CreateAccount')
                except EmailVerification.DoesNotExist:
                    pass
                
                messages.error(request, 'Invalid OTP. Please try again.')
                return render(request, "loging/otp_verification.html", {"form": form, "email": email})
        else:
            # Display form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return render(request, "loging/otp_verification.html", {"form": form, "email": email})


class CompleteRegistration(View):
    """Third step: Complete registration with user details"""
    
    def get(self, request):
        email = request.session.get('registration_email')
        if not email:
            messages.error(request, 'Please start the registration process again.')
            return redirect('loging:CreateAccount')
        
        # Check if email is verified
        try:
            verification = EmailVerification.objects.get(email=email, is_verified=True)
        except EmailVerification.DoesNotExist:
            messages.error(request, 'Please verify your email first.')
            return redirect('loging:verify_otp')
        
        form = CompleteRegistrationForm()
        return render(request, "loging/complete_registration.html", {"form": form, "email": email})
    
    def post(self, request):
        email = request.session.get('registration_email')
        if not email:
            messages.error(request, 'Please start the registration process again.')
            return redirect('loging:CreateAccount')
        
        # Check if email is verified
        try:
            verification = EmailVerification.objects.get(email=email, is_verified=True)
        except EmailVerification.DoesNotExist:
            messages.error(request, 'Please verify your email first.')
            return redirect('loging:verify_otp')
        
        form = CompleteRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = CustomUser.objects.create_user(
                    username=form.cleaned_data['username'],
                    email=email,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password'],
                    user_type=form.cleaned_data['user_type'],
                    email_verified=True
                )
                
                # Clean up verification record
                verification.delete()
                
                # Clear session
                if 'registration_email' in request.session:
                    del request.session['registration_email']
                
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('loging:loginView')
                
            except IntegrityError:
                messages.error(request, 'An account with this username already exists. Please use a different username.')
                return render(request, "loging/complete_registration.html", {"form": form, "email": email})
        else:
            # Display form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
            return render(request, "loging/complete_registration.html", {"form": form, "email": email})

class redirect_view(LoginRequiredMixin,View):
    def get(self,request):
        if hasattr(request.user, 'user_type'):
            if request.user.user_type == "Counsellor":
                date = timezone.now().date()
                if DailyLog_Counsellor.objects.filter(doctor=request.user.id,date=date).exists():
                     return redirect(reverse_lazy("loging:counsellor"))
                else:
                    return redirect(reverse_lazy("CounsellorIntern:daily_log_popup"))
            elif request.user.user_type == "patient":
                return redirect(reverse_lazy("userend:home"))
            elif request.user.user_type == "intern":
                return redirect(reverse_lazy("loging:intern"))
        return redirect(reverse_lazy("userend:home"))

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return render(request, "loging/logout.html")

class counsellor(View):
    def get(self, request):
        return render(request, "userend/dashboard.html")

class intern(View):
    def get(self, request):
        return render(request, "userend/genz_dashboard.html")