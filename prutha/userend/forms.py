from django import forms
from .models import Appointment
from CounsellorIntern.models import Psychologist
from django.core.validators import RegexValidator,EmailValidator,MaxValueValidator
from datetime import date, timedelta
from django.core.exceptions import ValidationError

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude=['user','IsPending','Assigned_doctor','date']  # Exclude date field as it will be auto-populated
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select your preferred date', 'value': '', 'autocomplete': 'off'}),
            'time_slot': forms.RadioSelect(attrs={'class': 'time-slot-radio'}),
            'selected_doctor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Choose your preferred doctor'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            # 'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select your preferred date'}),

            # 'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your 10-digit phone number'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your gender'}),
            'duration': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select session duration'}),
            'session_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select session type'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the choices for the doctor field
        try:
            self.fields['selected_doctor'].queryset = Psychologist.objects.all()
            self.fields['selected_doctor'].empty_label = "Select a Doctor"
        except Exception as e:
            # Temporarily handle database issues
            self.fields['selected_doctor'].queryset = Psychologist.objects.none()
            self.fields['selected_doctor'].empty_label = "No doctors available"
        
        # Set date constraints for 3-day limit
        today = date.today()
        max_date = today + timedelta(days=3)
        
        # Set min and max attributes for the date input and ensure no default value
        self.fields['appointment_date'].widget.attrs.update({
            'min': today.strftime('%Y-%m-%d'),
            'max': max_date.strftime('%Y-%m-%d'),
            'value': '',  # Explicitly set empty value
            'autocomplete': 'off'  # Prevent browser autofill
        })
    
    def clean_appointment_date(self):
        # Let the view handle date validation to provide better error messages
        appointment_date = self.cleaned_data.get('appointment_date')
        return appointment_date
    