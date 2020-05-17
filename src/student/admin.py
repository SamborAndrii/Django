from django.contrib import admin
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'group')

admin.site.register(Student, StudentAdmin)