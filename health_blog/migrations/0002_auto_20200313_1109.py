# Generated by Django 3.0.3 on 2020-03-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='instructions',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]