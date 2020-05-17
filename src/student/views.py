import random
import string

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from student.models import Student
from student.forms import StudentFormEdit


# Create your views here.
def hello(request):
    return HttpResponse('hello')


def gen_password(request):
    return HttpResponse(''.join([
        random.choice(string.ascii_letters)
        for _ in range(10)
    ]))


def students(request):
    queryset = Student.objects#.order_by('first_name')#.all()
    filter = request.GET.get('filter')
    if filter:
        students = queryset.order_by('-id').filter(
                Q(first_name__startswith=filter) |
                Q(last_name__startswith=filter) |
                Q(email__startswith=filter)
            )
    else:
        students = queryset.order_by('-id').all()

    students = students.select_related('group')

    return render(
        request=request,
        template_name='students.html',
        context={
            'students' : students,
            'title': 'Students'
        }
    )


def students_edit(request, id):
    student = Student.objects.get(id=id)

    if not student:
        return HttpResponseNotFound(f'Student with id {id} not found')

    if request.method == 'POST':
        form = StudentFormEdit(
            data=request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:

        form = StudentFormEdit(
            instance=student
        )

    return render(
        request=request,
        template_name='student_edit.html',
        context={
            'form' : form,
            'id' : id,
            'title': 'Student edit'
        }
    )


def students_add(request):

    if request.method == 'POST':
        form = StudentFormEdit(
            data=request.POST,
        )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students'))
    else:

        form = StudentFormEdit()

    return render(
        request=request,
        template_name='student_add.html',
        context={
            'form' : form,
            'title': 'Student add'
        }
    )

def students_delete(request, id):
    student = Student.objects.get(id=id)

    student.delete()

    return HttpResponseRedirect(reverse('students'))