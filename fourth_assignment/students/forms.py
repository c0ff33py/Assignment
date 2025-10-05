from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "gender", "phone_number"]
        widgets = {
            "name":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class": "form-control"}),
            "gender":forms.Select(attrs={"class": "form-select"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }
