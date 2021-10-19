from django import forms
from .models import Parcels


class OrderCreateForm(forms.ModelForm):
    treck = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'Ваш трек номер'}))
    parcels_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'Например Zara, HM'}))
    recipient = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'ФИО получателя'}))
    price = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','type':'text','placeholder':'0.00 $','step':0.05}))
    category = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'Например Техника'}))
    amount = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','type':'text','placeholder':'Количество товара'}))
    weight = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','type':'text','placeholder':'Вес товара','step':0.05}))
    country = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input country__input','type':'text','placeholder':'Выберите страну'}))
    web_site = forms.URLField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'www.primer.com'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input modal__textarea','placeholder':'Можете оставить комментарий'}))

    class Meta:
        model = Parcels
        fields = ['treck','parcels_name','recipient','price','category','amount','weight','country','web_site','comment']


class OrderUpdateForm(forms.ModelForm):
    treck = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'Ваш трек номер'}))
    parcels_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'Например Zara, HM'}))
    recipient = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'ФИО получателя'}))
    price = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','type':'text','placeholder':'0.00 $','step':0.05}))
    category = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'Например Техника'}))
    amount = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','type':'text','placeholder':'Количество товара'}))
    weight = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':'sign__input','type':'text','placeholder':'Вес товара','step':0.05}))
    country = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'sign__input country__input','type':'text','placeholder':'Выберите страну'}))
    web_site = forms.URLField(required=True,widget=forms.TextInput(attrs={'class':'sign__input','type':'text','placeholder':'www.primer.com'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'sign__input modal__textarea','placeholder':'Можете оставить комментарий'}))

    class Meta:
        model = Parcels
        fields = ['treck','parcels_name','recipient','price','category','amount','weight','country','web_site','comment']