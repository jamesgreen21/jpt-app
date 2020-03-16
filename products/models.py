from django.db import models


class Product(models.Model):
    TYPE = (
        ('class', 'Class'),
        ('item', 'Item'),
    )

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        upload_to='bookings_img',
        default='bookings_img/default.jpg',
    )
    product_type = models.CharField(
        max_length=30,
        choices=TYPE,
    )
    session_token = models.IntegerField(default=0)

    def __str__(self):
        return self.name
