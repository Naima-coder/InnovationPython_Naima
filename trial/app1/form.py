from django import forms
from .models import student
class form1(forms.Form):
    name=forms.CharField(label="Name",max_length=100)
    feedback=forms.CharField(label="FeedbaCK")
class mform(forms.ModelForm):
    class Meta:
        model= student
        fields=["name"]