from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


from .models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = '__all__'


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'name','email', 'phonenumber', 'location'}