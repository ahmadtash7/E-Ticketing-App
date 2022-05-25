from django.forms import ModelForm
from . import models
from django import forms


class UserForm(ModelForm):
    class Meta:


        model = models.User_Account
        fields = ['cms_id','first_name', 'last_name', 'email_address','password','contact_number']
        password = forms.CharField(max_length=32, widget=forms.PasswordInput())
        widgets = {
            'password': forms.PasswordInput(),
        }
