from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField("Address line 1", max_length=100, blank=False)
    street_address2 = models.CharField("Address line 2", max_length=100, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=12, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    county = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{}-{}-{}".format(self.quantity, self.product.name, self.product.price)
