from django import forms

from .models import Inquiry

class InquiryForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ('fullname', 'phonenumber', 'service', 
                  'complaint', 'department',)

class ResolveForm(forms.ModelForm):

    class Meta:
        model = Inquiry
        fields = ('comment', 'status',)
