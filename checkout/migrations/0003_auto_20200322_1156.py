# Generated by Django 3.0.3 on 2020-03-22 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200321_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address2',
            new_name='street_address2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='town_or_city',
        ),
    ]
