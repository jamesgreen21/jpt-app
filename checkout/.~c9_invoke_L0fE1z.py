from django.db import models
from products.models import Product


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address1 = models.CharField("Address line 1", max_length=1024, blank=False)
    address2 = models.CharField("Address line 2", max_length=1024, blank=False)
    city = models.CharField(max_length=1024, blank=False)
    postcode = models.CharField(max_length=12, blank=False)
    country = models.CharField(max_length=50, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, )
    products = models.ForeignKey(Product, null-False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{}-{}-{}".format(self.quantity, self.product.name, self.product.price)
