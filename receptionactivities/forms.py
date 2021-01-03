from django import forms
from datetime import date
current_date = date.today()
year = current_date.year
salutationchoices = [
    ('mr', 'Mr'),
    ('ms', 'Miss'),
    ('mrs', 'Mrs'),

]
genderchoice = [
    ('male', 'Male'),
    ('female', 'Female')
]


class NewPatient(forms.Form):
    salutation = forms.CharField(label="Salutation",required=True,
                                 widget=forms.Select(
                                     choices=salutationchoices,
                                     attrs={
                                         "class": "form-control",
                                         "name": "salutation",
                                         "id": "salutation",
                                         "tabindex" : "1"
                                     }
                                 )
                                 )
    firstname = forms.CharField(label="First Name",required=True,
                                widget=forms.TextInput(
                                    attrs={
                                        "class": "form-control",
                                        "placeholder": "First Name",
                                        "name": "firstname",
                                        "id": "firstname",
                                        "tabindex": "2"
                                    }
                                )
                                )
    middlename = forms.CharField(label="Middle Name",required=False,
                                 widget=forms.TextInput(
                                     attrs={
                                         "class": "form-control",
                                         "placeholder": "Middle Name",
                                         "name": "middlename",
                                         "id": "middlename",
                                         "tabindex": "3"

                                     }
                                 )
                                 )
    lastname = forms.CharField(label="Last Name",required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "Last Name",
                                       "name": "lastname",
                                       "id": "lastname",
                                       "tabindex": "4"

                                   }
                               )
                               )
    dob = forms.DateField(label="DOB",required=True,
                          widget=forms.SelectDateWidget(years=range(1910, year),
                              attrs={
                                  "name": "dob",
                                  "id": "dob",
                                  "tabindex": "5"

                              }
                          )
                          )

    phonenumber = forms.CharField(label="Phone Number",required=True,
                              widget=forms.TextInput(
                                  attrs={
                                      "class": "form-control",
                                      "placeholder": "Phone Number",
                                      "name": "phonenumber",
                                      "id": "phonenumber",

                                      "tabindex": "8"
                                  }
                              )
                              )
    email = forms.EmailField(label="Email",required=False,
                             widget=forms.EmailInput(
                                 attrs={
                                     "class": "form-control",
                                     "placeholder": "Email",
                                     "name": "email",
                                     "id": "email",
                                     "tabindex": "9"

                                 }
                             )
                             )
    addressline1 = forms.CharField(label="Address Line 1",required=True,
                                  widget=forms.TextInput(
                                      attrs={
                                          "class": "form-control",
                                          "placeholder": "Address Line 1",
                                          "name": "addressline1",
                                          "id": "addressline1",

                                          "tabindex": "10"

                                      }
                                  )
                                  )
    addressline2 = forms.CharField(label="Address Line 2",required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "class": "form-control",
                                           "placeholder": "Address Line 2",
                                           "name": "addressline2",
                                           "id": "addressline2",
                                           "tabindex": "11"

                                       }
                                   )
                                   )
    addressline3 = forms.CharField(label="Address Line 3",required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           "class": "form-control",
                                           "placeholder": "Address Line 3",
                                           "name": "addressline3",
                                           "id": "addressline3",
                                           "tabindex": "12"

                                       }
                                   )
                                   )

    location = forms.CharField(label="Location",required=False,
                                  widget=forms.TextInput(
                                      attrs={
                                          "class": "form-control",
                                          "placeholder": "Location",
                                          "name": "location",
                                          "id": "location",
                                          "tabindex": "13"

                                      }
                                  )
                                  )
    postcode = forms.CharField(label="P O Code",required=False,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "P O Code",
                                       "name": "postcode",
                                       "id": "postcode",
                                       "tabindex": "17"

                                   }
                               )
                               )
    state = forms.CharField(label="State",required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "State",
                                       "name": "state",
                                       "id": "state",
                                       "required": "required",
                                       "tabindex": "14"

                                   }
                               )
                               )
    city = forms.CharField(label="City",required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "City",
                                       "name": "city",
                                       "id": "city",
                                       "required": "required",
                                       "tabindex": "14"


                                   }
                               )
                               )
