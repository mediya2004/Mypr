from django import forms
from . models import registrationform
class registrationform1(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=registrationform
        fields='__all__'

class loginform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=registrationform
        fields=('email','password')
class updateForm(forms.ModelForm):
    class Meta():
        model=registrationform
        fields=('name','age','place','email')

class ChangepasswordForm(forms.Form):
    Oldpassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)