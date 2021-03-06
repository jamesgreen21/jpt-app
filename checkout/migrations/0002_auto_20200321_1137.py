# Generated by Django 3.0.3 on 2020-03-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='county',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(max_length=100, verbose_name='Address line 1'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(max_length=100, verbose_name='Address line 2'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=40),
        ),
    ]
