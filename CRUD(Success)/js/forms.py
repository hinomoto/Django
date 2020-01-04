from django import forms
from .models import Color
 
 
class ColorForm(forms.Form):
    color = forms.ModelChoiceField(
        queryset=Color.objects.all(),
        empty_label=None,
        required=False, 
    )