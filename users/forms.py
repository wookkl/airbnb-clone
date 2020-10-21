from django import forms
from . import models


class LoginForm(forms.Form):

    """ Login Form Definition """

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong. "))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User deos not exits."))


class SignUpForm(forms.Form):

    """ SignUp Form Definition """

    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.get(email=email)
            raise forms.ValidationError("User already exists with that email.")

        except models.User.DoesNotExist:
            return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password confirmation does not match.")
        else:
            return confirm_password
