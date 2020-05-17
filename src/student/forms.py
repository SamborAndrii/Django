from django.core.exceptions import ValidationError
from django.forms import ModelForm
from student.models import Student


class StudentFormEdit(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    # def clean_email(self):
    #
    #     email = self.cleaned_data['email']
    #
    #     already_exists = Student.objects. \
    #         filter(email=email). \
    #         exclude(id=self.instance.id). \
    #         count() > 0
    #
    #     if already_exists:
    #         raise ValidationError('Email already exists!')
    #
    #     return email