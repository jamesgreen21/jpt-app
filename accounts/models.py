from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', "Don't specify"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        "Upload a profile picture (optional)",
        default='profile_pics/default.jpg',
        upload_to='profile_pics'
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICE, default='Unknown')
    address1 = models.CharField("Address line 1", max_length=1024, null=True)
    address2 = models.CharField("Address line 2", max_length=1024, null=True)
    city = models.CharField(max_length=1024, null=True)
    postcode = models.CharField( max_length=12, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
    
        img = Image.open(self.image.path)
    
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
