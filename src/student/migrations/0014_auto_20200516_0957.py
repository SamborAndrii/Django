# Generated by Django 3.0.5 on 2020-05-16 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_logger'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Logger',
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=datetime.date(2020, 5, 16)),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=64, unique=True),
        ),
    ]