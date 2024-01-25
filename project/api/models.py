from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (('admin', 'ادمین'),('doctor', 'دکنر'),('patient', 'بیمار'),('nurse', 'پرستار'))
    SEX_CHOICES = (('male', 'مرد'),('female', 'زن'))
    EXPERTISE_CHOICES = (('orthopedics', 'ارتوپدی'),('digestion', 'گوارش'),('kidney', 'کلیه'),('ear_nose_throat', 'گوش و حلق و بینی'),
                         ('neurosurgery', 'جراحی اعصاب'),('general_surgery', 'جراحی عمومی'),('psychology', 'روانشناسی'),
                         ('ophthalmology', 'چشم پزشکی'),('heart', 'قلب'),('rheumatology', 'روماتولوژی'),('glands', 'غدد'),
                         ('children', 'اطفال'),('infectious_diseases', 'بیماری های عفونی'),('blood', 'خون'),('skin', 'پوست'),
                         ('dental', 'دندانپزشکی'),('laboratory', 'آزمایشگاه'),('photography', 'تصویربرداری'))

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_number = models.CharField(max_length=200)
    personnel_number = models.CharField(max_length=200, blank=True)
    birthdate = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.TextField(default='')
    expertise = models.CharField(max_length=200, choices=EXPERTISE_CHOICES, blank=True)
    attend_time = models.CharField(max_length=200, blank=True)
    sex =  models.CharField(max_length=200, choices=SEX_CHOICES, default='male')

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)