from django import forms
from django.contrib.auth import get_user, get_user_model, login, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'sign__input', 'placeholder':'Email или ваша почта!'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'sign__input','placeholder':'Пароль'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'sign__input','placeholder':'Повторите пароль'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Фамилия'}))
    before_last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Отчество'}))
    address_living = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Аддрес проживание'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Город'}))
    number_of_address = forms.CharField(widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'номер'}))
    postal_code = forms.CharField(widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'индекс'}))
    # passport_out = forms.CharField(required=True, widget=forms.NumberInput(attrs={'type': 'file', 'class': 'sign__input ','name': '','accept': 'image/*'}))
    # passport_in = forms.ImageField(required=True, widget=forms.FileInput(attrs={'type': 'file','class': 'sign__input file__upload','id': 'scan-in','name': '','accept': 'image/*'}))

    phone_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Ваш номер телефона'}))
    telegram = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'@Nickname'}))

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password',
                   'password_confirm', 'last_name', 'before_last_name',
                   'address_living', 'city', 'number_of_address',
                   'postal_code', 'telegram', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError('Такой аккаунт уже Существует')
        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.pop('password_confirm')
        if not password == password_confirm:
            raise forms.ValidationError('Пароли не совпадает!')
        return self.cleaned_data

    def clean_pass(self):
        if UserRegistrationForm == '':
            raise forms.ValidationError('asdfasdfsadf')
        return self.cleaned_data



class SignForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': 'Email или ваша почта' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'sign__input', 'placeholder': 'Пароль!!' }))


    def clean_email(self):
        data = self.cleaned_data
        email = data['email']
        if email:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Email не найден попробуйте снова')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        email = self.cleaned_data.get('email')
        if password and email:
            qs = User.objects.filter(email=email)[0]
            if not check_password(password, qs.password):
                raise forms.ValidationError('Неверный пароль')
        return password

    def get_user(self):
        from django.contrib.auth import authenticate
        return authenticate(
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)








