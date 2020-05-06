from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from student.forms import StudentAddForm
from student.models import Student


# Create your views here.
def students_list(request):
    qs = Student.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    result = '<br>'.join(
        str(student)
        for student in qs
    )

    # return HttpResponse(result)
    return render(        request=request,
        template_name='students_list.html',
        context={'students_list' : result}
    )


def students_add(request):

    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            student = form.save()
            print(f'Student created: {student}')
            return HttpResponseRedirect(reverse('students'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={'form' : form}
    )
