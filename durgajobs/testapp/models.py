from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=40)
    phonno=models.IntegerField()
class BloreJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=40)
    phonno=models.IntegerField()
class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=64)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=60)
    email=models.CharField(max_length=40)
    phonno=models.IntegerField()

    #def __str__(self):
     #  return self.ename
