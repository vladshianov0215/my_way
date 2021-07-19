from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"] #like attributes from MODEK (task)
        widgets  = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':"Put name of task zzzzzz"
            }),
            "task": Textarea(attrs={
            'class': 'form-control',
            'placeholder':"Put text zzzzzzz"
            })
            }