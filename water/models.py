from django.db import models


class Water(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена за 1 бутылку")
    is_in_stock = models.BooleanField(verbose_name="Есть на складе?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялось значение акциия?")

class NewWater(models.Model):
    src = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)