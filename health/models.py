from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Signup(models.Model):
    fullname = models.CharField(max_length=50, blank=True)
    username=models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=20, blank=True)
    altphone = models.CharField(max_length=20, blank=True)
    password=models.CharField(max_length=30, blank=True)
    gender=models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=50, blank=True)
    aadhar=models.CharField(max_length=50, blank=True)
    dob = models.CharField(max_length=50, blank=True)
    profile = models.FileField(blank=True)
    role=models.CharField(max_length=50,blank=True,default="patient")


    def __str__(self):
        return self.fullname

class Userdata(models.Model):
    aadhar = models.CharField(max_length=50, blank=True)
    comments= models.CharField(max_length=2000, blank=True)
    time=models.CharField(max_length=100,blank=True)
    progressnotes=models.CharField(max_length=500,blank=True)
    vitalsigns=models.CharField(max_length=500,blank=True)
    diagnoses=models.CharField(max_length=500,blank=True)
    immunizationdates=models.CharField(max_length=500,blank=True)
    doctorname=models.CharField(max_length=500,blank=True)
    hospitalname=models.CharField(max_length=500,blank=True)
    prescription=models.CharField(max_length=500,blank=True)
    caop=models.CharField(max_length=500,blank=True)
    mobileno=models.CharField(max_length=20,blank=True)
    prescription1 = models.FileField(blank=True)
    prescription2 = models.FileField(blank=True)
    prescription3 = models.FileField(blank=True)
    Labtest=models.CharField(max_length=500,blank=True)
    allergies=models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.aadhar
