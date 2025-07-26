import datetime
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'reminder_time']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'min': datetime.date.today().isoformat()  # 👈 sets today as the minimum
                }
            ),
            'reminder_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

