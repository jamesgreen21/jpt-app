# Generated by Django 3.0.3 on 2020-02-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('headline', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='blog_pics/default.jpeg', upload_to='blog_pics')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
