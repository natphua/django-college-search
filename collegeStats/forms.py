from django import forms
from .models import College


class collegeForm(forms.ModelForm):  # creating a form based on College model
    class Meta:
        # specify model to be used
        model = College
        # specify fields to be used
        fields = ['college_name']
