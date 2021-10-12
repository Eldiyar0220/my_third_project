from django import forms
from django.contrib.auth import get_user, get_user_model, login, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import context
from django.template.loader import render_to_string
from django.urls import reverse

User = get_user_model()

# def send_activation_mail(email):
#     message = f'http://127.0.0.1:8000/account/activate/'
#     send_mail('Активация аккаунта', message, 'test@gmail.com', [email])

def send_activation_mail(email, activation_code):
    message = f'http://127.0.0.1:8000/accounts/activation/?u={activation_code}'
    send_mail('Активация аккаунта', message, 'test@gmail.com', [email])


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

    postal_code_message = 'Должен быть в формате: XXX XXX'
    postal_code_regex = RegexValidator(
        regex=r'^\d{6}$',
        message=postal_code_message
    )

    postal_code = forms.CharField(validators=[postal_code_regex],max_length=6, widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'индекс'}))
    # passport_out = forms.CharField(required=True, widget=forms.NumberInput(attrs={'type': 'file', 'class': 'sign__input ','name': '','accept': 'image/*'}))
    # passport_in = forms.ImageField(required=True, widget=forms.FileInput(attrs={'type': 'file','class': 'sign__input file__upload','id': 'scan-in','name': '','accept': 'image/*'}))

    phone_message = 'Формат номера: 996 999 999 999'
    phone_regex = RegexValidator(
        regex="(996)",
        message=phone_message
    )
    phone_number = forms.CharField(validators=[phone_regex],required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Ваш номер телефона'}))

    telegram_message = 'должно начинатся с @'
    telegram_regex = RegexValidator(
        regex="(@)",
        message=telegram_message
    )
    telegram = forms.CharField(validators=[telegram_regex],required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'@Nickname'}))

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
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        password = self.cleaned_data['password']
        if validate_password(password):
            raise forms.ValidationError('Пароли не совпа')
        return self.cleaned_data


    # def clean(self):
    #     data = self.cleaned_data
    #     if data['password'] != data['password_confirm']:
    #         raise forms.ValidationError('Пароли не совпадают!!')
    #     password = data['password']
    #     if validate_password(password):
    #         raise forms.ValidationError('Пароли не совпа')
    #     return self.cleaned_data

    def save(self):
        user = User.objects.create(**self.cleaned_data)
        user.create_activation_code()
        send_activation_mail(user.email, user.activation_code)
        return user


class SignForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': 'Email или ваша почта' }))
    password = forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={ 'class': 'sign__input', 'placeholder': 'Пароль!!' }))

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



class ResetForm(forms.Form):

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Ваш новый пароль'
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': 'sign-password',
        'class': 'sign__input',
        'placeholder': 'Повторите новый пароль'
    }))

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password2']

    def clean(self):
        data = self.cleaned_data
        password = data['password']
        if validate_password(password):
            raise forms.ValidationError('Введите более защищённый пароль')
        return super().clean()






