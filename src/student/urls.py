from django.urls import path
from student.views import students, students_edit, students_add, students_delete

urlpatterns = [
    path('', students, name='students'),
    path('add/', students_add, name='student-add'),
    path('edit/<int:id>', students_edit, name='student-edit'),
    path('delete/<int:id>', students_delete, name='student-delete'),
]