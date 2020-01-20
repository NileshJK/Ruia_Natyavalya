from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

Gender = (('male','Male'),('female','Female'))
Audition = (('drama','Drama'),('dance','Dance'))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    General_Registration_No = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','General_Registration_No','password1','password2']

#class ProfileForm(forms.Form):
    #Name = forms.CharField()
    #email = forms.EmailField(label='E-Mail')
    #Gender = forms.ChoiceField(choices=Gender)
    #Branch = forms.CharField()
    #General_RNo = forms.CharField()
    #Audition = forms.ChoiceField(choices=Audition)
    #Upload_File = forms.FileField
