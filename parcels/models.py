from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey

User = get_user_model()

STATUS_CHOICE=[
    ('unregistered_order','незарегистрированный заказ'),
    ('during','в процессе'),
    ('sorting','сортировка'),
    ('processed_1','обработан1'),
    ('processed_2','обработан2'),
    ('processed_3','обработан3'),
    ('In_stock_in_KG1','на складе в Kg1'),
    ('In_stock_in_KG2','на складе в Kg2'),
    ('In_stock_in_KG3','на складе в Kg3'),
]

class Parcels(models.Model):
    order = ForeignKey(User, on_delete=models.CASCADE, default=True)
    date = models.DateField(blank=False, auto_now=True)
    recipient = models.CharField(max_length = 100)
    parcels_name = models.CharField(null = False, max_length = 100)
    amount = models.PositiveIntegerField(null = True)
    price = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)
    weight = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100, verbose_name=u"Страна")
    treck = models.CharField(max_length=50, null=False, unique=True, default=0)
    category = models.CharField(max_length=100,null=False,default=False)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default="unregistered_order")
    web_site = models.URLField(max_length=200,null=False,default=False)
    comment = models.TextField(max_length=324,null=True)

    def __str__(self):
        return f'Owner: {self.order} -> {self.parcels_name}'