from django.shortcuts import render, redirect
from django.http import HttpResponse
from formApp.form import PartnerForm, FacultyForm, CourseForm
from .models import Faculty, Course

# Create your views here.

def display(request):
    return render(request, 'index0.html')

def addFaculty(request):
    faculty = FacultyForm()
    if request.method == 'POST':
        faculty = FacultyForm(request.POST)
        if faculty.is_valid():
                 faculty.save()
        return redirect('/facultyList')
#     if id:
#         faculty = Faculty.objects.filter(id=id)
    return render(request, 'faculty.html', {'faculty': faculty})

def updateFacultyDetails(request, id):
    faculty = Faculty.objects.filter(id=id)
    return render(request, 'faculty.html', {'faculty': faculty})

def facultyList(request):
    faculties = Faculty.objects.all()
    return render(request, 'facutyList.html', {'faculties': faculties})

def addCourse(request):
    course = CourseForm()
    if request.method == 'POST':
        course = CourseForm(request.POST)
        if course.is_valid():
                 course.save()
        return redirect('/courseList')
    return render(request, 'course.html', {'course': course})

def courseList(request):
    courses = Course.objects.all()
    return render(request, 'courseList.html', {'courses': courses})

def partnerData(request):
    partner = PartnerForm()
#     faculty = FacultyForm()
    if request.method == 'POST':
        partner = PartnerForm(request.POST)
#         faculty = Faculty(request.POST)
#         form = {'partner': partner, 'faculty': faculty}
        if partner.is_valid():
            partner.save()
#         if faculty.is_valid():
#             faculty.save()
        return redirect('/partner')
    return render(request, 'index0.html', {'partner': partner})