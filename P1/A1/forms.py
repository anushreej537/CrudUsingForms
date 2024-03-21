from django import forms
from A1.models import emp,User


class EmpForm(forms.ModelForm):
    class Meta:
        model = emp
        fields = '__all__'

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']