from Congresso.models import Users
from django import forms
from django.forms import ModelForm

class LoginForm(ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'user',
        'maxlength': '16'
    }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'pass',
        'maxlength': '255'
    }))
    class Meta:
        model = Users
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha']