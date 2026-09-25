from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["input_text"]
        labels = {
            "input_text": "Text to process",
        }