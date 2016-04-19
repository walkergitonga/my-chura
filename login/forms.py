from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    DEPARTMENTS = (
        ('CUSTOMER CARE', 'Customer Care'),
        ('SALES', 'Sales'),
        ('DESIGN', 'Design'),
        ('DEVELOPMENT', 'Development'),
        ('MAINTENANCE', 'Maintenance'),
    )
    department   = forms.ChoiceField(choices=DEPARTMENTS)
    email = forms.EmailField(required=True)
    fullname = forms.CharField(max_length=80, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'department', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.fullname = self.cleaned_data['fullname']
        user.email = self.cleaned_data['email']
        user.department = self.cleaned_data['department']
        
        if commit:
            user.save()
            
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())