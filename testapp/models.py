from django.db import models

# Create your models here.
class EnquiryModel(models.Model):
	name=models.CharField(max_length=32)
	email=models.EmailField()
	phone=models.IntegerField()
	message=models.CharField(max_length=200)
class Jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=64)
    eligibility=models.CharField(max_length=64)
    address=models.CharField(max_length=64)
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return self.title
class Apply(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Gender=models.CharField(max_length=2)
    Designation=models.CharField(max_length=70)
    Location=models.CharField(max_length=20)
    DOB=models.DateField()
    Qualification=models.CharField(max_length=20)
    Experience=models.IntegerField()
    Language=models.CharField(max_length=20)
    Nationality=models.CharField(max_length=20)
    year_of_passout=models.IntegerField()
    job_type=models.CharField(max_length=20)
    current_ctc=models.FloatField()
    expected_ctc=models.FloatField()

  