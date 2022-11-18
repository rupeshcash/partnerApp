from django.urls import path
from . import views
urlpatterns = [
	path('home/', views.display, name = "Home"),
	path('partner/', views.partnerData, name = "pd"),
	path('addFaculty/', views.addFaculty, name = 'addFaculty'),
	path('facultyList/', views.facultyList, name= 'facultyList'),
	path('updateFacultyDetails/<int:id>', views.updateFacultyDetails, name= 'updateFacultyDetails'),
	path('addCourse/', views.addCourse, name = 'addCourse'),
    path('courseList/', views.courseList, name= 'courseList'),
]