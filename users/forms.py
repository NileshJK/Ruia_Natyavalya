from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

Gender = (('male','Male'),('female','Female'))
Audition = (('drama','Drama'),('dance','Dance'))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    General_Registration_No = forms.CharField()
    Gender = forms.ChoiceField(choices=Gender)
    Branch = forms.CharField()
    Audition = forms.ChoiceField(choices=Audition)
    class Meta:
        model = User
        fields = ['username','email','General_Registration_No','Gender','Branch','Audition','password1','password2']

#class ProfileForm(forms.Form):
    #Name = forms.CharField()
    #email = forms.EmailField(label='E-Mail')
    
    #Upload_File = forms.FileField
