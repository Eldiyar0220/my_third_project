from django import forms

from accounts.models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'sign__input required','type':'text','id':"reg-email", 'name':"reg-email", 'placeholder':'Email или ваша почта'}))
    password = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'sign__input','placeholder':'Пароль'}))
    password_confirm = forms.CharField(min_length=8,required=True,widget=forms.PasswordInput(attrs={'class':'sign__input','placeholder':'Повторите пароль'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'имя'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Фамилия'}))
    before_last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Отчество'}))
    address_living = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Аддрес проживание'}))
    city = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','placeholder':'Город'}))
    number_of_address = forms.CharField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'номер'}))
    postal_code = forms.CharField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'индекс'}))
    # passport_out = forms.CharField(required=True, widget=forms.NumberInput(attrs={'type': 'file', 'class': 'sign__input ','name': '','accept': 'image/*'}))
    # passport_in = forms.ImageField(required=True, widget=forms.FileInput(attrs={'type': 'file','class': 'sign__input file__upload','id': 'scan-in','name': '','accept': 'image/*'}))
    phone_number = forms.CharField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','placeholder':'Ваш номер телефона'}))
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
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадает!')
        return self.cleaned_data