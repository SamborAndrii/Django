# Generated by Django 3.0.5 on 2020-05-16 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20200516_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
