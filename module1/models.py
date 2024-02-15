from django.db import models

# Create your models here.
class faculty(models.Model):
    username = models.IntegerField(max_length=4)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=150)
    class Meta:
         db_table="faculty"


class student(models.Model):
    username = models.IntegerField(max_length=10)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=150)
    class Meta:
         db_table="student"

class teamdetails(models.Model):
    PFSDTeamName = models.CharField(max_length=100)
    CLUSTER = models.IntegerField(max_length=2)
    TEAM = models.IntegerField(max_length=2)
    StudentID = models.IntegerField(max_length=20)
    TeamLead = models.CharField(max_length=20)
    BusinessSystem  = models.CharField(max_length=100)
    FacultyMentor = models.CharField(max_length=100)
    class Meta:
         db_table="teamdetails"

class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(primary_key = True)
    comments = models.TextField(max_length=255)
    class Meta:
        db_table="contactus"

class datetime1(models.Model):
    time12 = models.TextField(max_length=255)
    class Meta:
        db_table="datetime1"

# weather/models.py

from django.db import models

class WeatherReport(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    weather_description = models.CharField(max_length=200)



