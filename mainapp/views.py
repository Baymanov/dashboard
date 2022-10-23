from django.shortcuts import render, redirect
from .models import *
from .forms import StudentCreateForm


# Create your views here.

def dashboard(request):
    return render(request, 'mainapp/dashboard.html')


def tables(request):
    mentors = Mentor.objects.all()
    students = Student.objects.all()
    context = {
        "mentors": mentors,
        "students": students
    }
    return render(request, 'mainapp/student_tables.html', context)


def create_student(request):
    form = StudentCreateForm()
    if request.method == "POST":
        form = StudentCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tables")
    else:
        form = StudentCreateForm()  

    context = {
        "form" : form
    }
    return render(request, "mainapp/create_student.html", context)

def update_student(request, pk):
    student = Student.objects.get(id=pk)
    form  = StudentCreateForm(instance=student)
    if request.method == "POST":
        form = StudentCreateForm(request.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect('tables')

    context = {
        "form" : form
    }

    return render(request, "mainapp/create_student.html", context)




def billing(request):
    return render(request, 'mainapp/billing.html')


def profile(request):
    return render(request, 'mainapp/profile.html')


def rtl(request):
    return render(request, 'mainapp/rtl.html')


def sign_in(request):
    return render(request, 'mainapp/sign_in.html')


def sign_up(request):
    return render(request, 'mainapp/sign_up.html')


def virtual_reality(request):
    return render(request, 'mainapp/virtual_reality.html')
