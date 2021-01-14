from django import forms
from .models import modelclass
class blogform(forms.ModelForm):
    class Meta:
        model=modelclass
        fields="__all__"