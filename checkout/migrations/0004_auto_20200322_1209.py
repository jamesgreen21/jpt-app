# Generated by Django 3.0.3 on 2020-03-22 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200322_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='products',
            new_name='product',
        ),
    ]