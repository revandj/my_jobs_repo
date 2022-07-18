from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company_name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=30)
    addrs=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.BigIntegerField()

class BngJobs(models.Model):
    date=models.DateField()
    company_name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=30)
    addrs=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.BigIntegerField()

class PuneJobs(models.Model):
    date=models.DateField()
    company_name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=30)
    addrs=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.BigIntegerField()
