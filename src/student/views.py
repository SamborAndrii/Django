from django.http import HttpResponse
from django.shortcuts import render
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
    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list' : result}
    )
