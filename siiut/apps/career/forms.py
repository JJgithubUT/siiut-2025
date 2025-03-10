from django import forms
from .models import Quarter

class QuarterForm(forms.ModelForm):
    class Meta:
        model = Quarter
        fields = ['quarter', 'quarter_name']
        widgets = {
            'quarter': forms.TextInput(attrs={"type": "number", "class": 'border border-gray-300 p-2 rounded-xl'}),
            'quarter_name': forms.TextInput(attrs={"class": 'border border-gray-300 p-2 rounded-xl'})
        }