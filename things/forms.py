"""Forms of the project."""
from dataclasses import field, fields
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
                'description': forms.Textarea(),
                'quantity': forms.NumberInput()
            }
# Create your forms here.
