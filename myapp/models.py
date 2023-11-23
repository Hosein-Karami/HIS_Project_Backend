from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    PATIENT = 1
    DOCTOR = 2
    PHARMACY = 3

    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (PHARMACY, 'Pharmacy'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False)


class file(models.Model):
    blood_group = models.CharField(max_length=3, blank=False, null=False)
    description = models.CharField(max_length=500)
    drug_sensitive = models.CharField(max_length=500)


class patient(models.Model):
    MALE = 1
    FEMALE = 2
    TRANS = 3

    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANS, 'Trans'),
    )

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    father_name = models.CharField(max_length=30, blank=False, null=False)
    insurance_type = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    national_id = models.CharField(max_length=15, blank=False, null=False)
    address = models.CharField(max_length=200)
    birthdate = models.DateField(blank=False, null=False)
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, blank=False, null=False)
