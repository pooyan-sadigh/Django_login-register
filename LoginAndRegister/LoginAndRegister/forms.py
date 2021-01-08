from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your user name"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )


class RegisterForm(forms.Form):
    error_css_class = 'text-danger'
    required_css_class = 'required'
    userName = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "enter your user name"})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "enter your email"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password"})
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "enter your password again"})
    )

    def clean_userName(self):
        userName = self.cleaned_data.get("userName")
        qs = User.objects.filter(username=userName)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return userName

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords do not match")

        return data
