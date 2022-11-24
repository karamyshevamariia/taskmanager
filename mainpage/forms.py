from django.forms import ModelForm, TextInput, Textarea

from mainpage.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['tittle', 'task']
        widgets = {
                      'tittle':TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите название'
        }),
        'task': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите задачу'
        })
        }
