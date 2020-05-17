from django.db import models

# Create your models here.
from faker.generator import random


class Group(models.Model):
    name = models.CharField(max_length=64)
    course = models.CharField(max_length=64)

    @classmethod
    def generate_group(cls):

        group = cls(
            name = f'Group {random.choice([1,2,3,4,5])}',
            course = random.choice([
                "IT 210: Web Application Development.",
                "IT 226: Enterprise Information Systems.",
                "IT 227: E-Commerce Technologies.",
                "IT 238: Networking and Client/Server Computing.",
                "IT 280: Internet Security.",
                "IT 295: IT-Based Application Project.",
                "IT 299: Graduate Seminar.",
            ])
        )

        group.save()

    def __str__(self):
        return f'{self.name} - {self.course}'