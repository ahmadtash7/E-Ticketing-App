from django.forms import ModelForm
from . import models
from django import forms


class UserForm(ModelForm):
    class Meta:


        model = models.User_Account
        fields = ['username','first_name', 'last_name', 'email','password','contact_number']
        password = forms.CharField(label='Password',max_length=32, widget=forms.PasswordInput())
        # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput())
        widgets = {
            'password': forms.PasswordInput(),
        }


    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match")
    #     return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# class FilterForm(forms.Form):
