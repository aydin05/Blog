from django import forms
from core.models import *
from django_countries.fields import CountryField


class SubscribeForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'name': 'name',
                'placeholder': 'Your Name',
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'name': 'email',
                'placeholder': 'Your Email'
            }))

    class Meta:
        model = SubscribeNews
        fields = '__all__'


class CallBackForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'full_name': 'full_name',
                'placeholder': 'Full name'
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'name': 'email',
                'placeholder': 'Email'
            }))
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'name': 'phone_number',
                'placeholder': 'Phone Number'
            }))

    class Meta:
        model = CallBack
        fields = '__all__'
