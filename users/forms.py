from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "login-input", "placeholder": "E-mail", "label": ""},
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "login-input", "placeholder": "Password", "label": ""}
        )
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 틀렸습니다."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("이메일이 존재하지 않습니다."))
