from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
                attrs={
                    "class":"form-control",
                    "name":"username",
                    "id":"username",
                    "placeholder":"Username"
                }))
    password = forms.CharField(widget=forms.PasswordInput(
                attrs={
                    "class":"form-control",
                    "name":"password",
                    "id":"password",
                    "placeholder": "Password"
                }))




