from django import forms

userchoices = [
    ('admin', 'Admin'),
    ('doctor', 'Doctor'),
    ('receptionist', 'Receptionist'),

]


class Adduser(forms.Form):
    usertype = forms.CharField(label="User Type",
                               widget=forms.Select(
                                   choices=userchoices,
                                   attrs={
                                       "class": "form-control",
                                       "name": "usertype",
                                       "id": "usertype",
                                       "required": "required"
                                   }
                               )
                               )
    name = forms.CharField(label="User Name",
                           widget=forms.TextInput(
                               attrs={
                                   "class": "form-control",
                                   "placeholder": "Name",
                                   "name": "username",
                                   "id": "username",
                                   "required": "required"
                               }
                           )
                           )
    email = forms.EmailField(label="Email",
                           widget=forms.EmailInput(
                               attrs={
                                   "class": "form-control",
                                   "placeholder": "Email",
                                   "name": "email",
                                   "id": "email",
                                   "required": "required"
                               }
                           )
                           )
    password = forms.CharField(label="Password",
                             widget=forms.PasswordInput(
                                 attrs={
                                     "class": "form-control",
                                     "placeholder": "Password",
                                     "name": "password",
                                     "id": "password",
                                     "required": "required"
                                 }
                             )
                             )

