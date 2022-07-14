from pyexpat import model
from django import forms
from .models import Tasks
from django.forms import ModelForm
from django import forms

class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        #fields = '__all__'
        fields = ['id','title','complete','starting_date']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':'enter task name'}),
            'starting_date':forms.DateInput( attrs={'placeholder':'Select a date', 'type':'date'}),
        }