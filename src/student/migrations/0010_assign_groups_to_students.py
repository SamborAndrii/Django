# Generated by Django 3.0.5 on 2020-05-09 10:24
import random

from django.db import migrations


def forward(apps, schema_editor):
    Group = apps.get_model('group', 'Group')
    Student = apps.get_model('student', 'Student')
    groups = [
        group
        for group in Group.objects.all().only('id')
    ]

    for student in Student.objects.all().only('group'):  # .iterator():
        student.group = random.choice(groups)
        student.save(update_fields=['group'])


def backward(apps, schema_editor):
    Student = apps.get_model('student', 'Student')
    for student in Student.objects.all().only('id', 'group'):  # .iterator():
        student.group = None
        student.save(update_fields=['group'])

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_student_group'),
    ]

    operations = [
        migrations.RunPython(
            code=forward,
            reverse_code=backward
        )
    ]