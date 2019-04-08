from django import forms
from empApp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
        'dob' : forms.DateInput(attrs={'class': 'datepicker1'}),
        'photo': forms.FileInput(attrs={'onchange': 'readURL(this);'}),
        
        }
