from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': 'имя' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': 'Фамилия' }))
    before_last_name = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': 'Отчество' }))
    address_living = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'sign__input',
            'placeholder': 'Аддрес проживание' }))
    city = forms.CharField(widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': 'Город' }))
    number_of_address = forms.CharField(
        widget=forms.NumberInput(attrs={ 'class': 'sign__input', 'placeholder': 'номер' }))

    postal_code_message = 'Должен быть в формате: XXX XXX'
    postal_code_regex = RegexValidator(
        regex=r'^\d{6}$',
        message=postal_code_message
    )

    postal_code = forms.CharField(min_length=6, max_length=6,
                                  widget=forms.NumberInput(attrs={ 'class': 'sign__input', 'placeholder': 'индекс' }))
    # passport_out = forms.CharField(required=True, widget=forms.NumberInput(attrs={'type': 'file', 'class': 'sign__input ','name': '','accept': 'image/*'}))
    # passport_in = forms.ImageField(required=True, widget=forms.FileInput(attrs={'type': 'file','class': 'sign__input file__upload','id': 'scan-in','name': '','accept': 'image/*'}))

    phone_message = 'Формат номера: 996 999 999 999'
    phone_regex = RegexValidator(
        regex="(996)",
        message=phone_message
    )
    phone_number = forms.CharField(validators=[phone_regex], widget=forms.TextInput(
        attrs={ 'class': 'sign__input', 'placeholder': 'Ваш номер телефона' }))

    telegram_message = 'должно начинатся с @'
    telegram_regex = RegexValidator(
        regex="(@)",
        message=telegram_message
    )
    telegram = forms.CharField(validators=[telegram_regex], required=True,
                               widget=forms.TextInput(attrs={ 'class': 'sign__input', 'placeholder': '@Nickname' }))

    class Meta:
        model = User
        fields = [ 'username',  'last_name', 'before_last_name', 'address_living', 'city', 'number_of_address', 'postal_code' ,'phone_number', 'telegram']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if email != qs:
    #         raise forms.ValidationError('вам отправно письмо, потвердите!!')
    #     return email

