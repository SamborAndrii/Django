import datetime

from faker import Faker
from django.db import models

# Create your models here.
from group.models import Group


class Student(models.Model):
    # class Meta:
    #     db_table = 'students'
    #      # abstract = True

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    birthdate = models.DateField(default=datetime.datetime.now().date())
    group = models.ForeignKey(
        to=Group,
        null=True,
        on_delete=models.CASCADE
    )

    @classmethod
    def generate_dummy(cls):
        faker = Faker()

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()

        st = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        st.save()

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}'
