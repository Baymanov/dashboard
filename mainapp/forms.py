from django import forms
from django.forms import fields
from .models import Student


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", "birth_date", "phone", "email", "group", "payment_status"]

