from django.db import models

# Create your models here.


class Partner(models.Model):
    institute_name = models.CharField(max_length=30, primary_key=True)
    image = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    no_of_students = models.IntegerField()

class Faculty(models.Model):
    institute_name = models.ForeignKey('Partner', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    experience = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

class Course(models.Model):
    institute_name = models.ForeignKey('Partner', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    fee = models.IntegerField()

class DemoVideos(models.Model):
    institute_name = models.ForeignKey('Partner', on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=30)
    path = models.CharField(max_length=20)

class TopRankers(models.Model):
    institute_name = models.ForeignKey('Partner', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=20)
    video = models.CharField(max_length=40)

class Scholarship(models.Model):
    institute_name = models.ForeignKey('Partner', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
