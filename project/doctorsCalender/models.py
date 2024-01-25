from django.db import models
from api.models import CustomUser

class Appointment(models.Model):
  doctor = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
  data = models.JSONField()