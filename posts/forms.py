from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        data = self.cleaned_data

        user = super(RegistrationForm, self).save()
        return user