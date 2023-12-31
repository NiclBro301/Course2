# Generated by Django 4.2.5 on 2023-11-22 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_students_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2023, 11, 22, 8, 58, 46, 11015)),
        ),
    ]
