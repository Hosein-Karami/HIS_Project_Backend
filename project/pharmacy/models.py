from django.db import models

class Medicine(models.Model):
  name = models.CharField(max_length=200)
  dose = models.IntegerField()
  type = models.CharField(max_length=200)
  expire_date = models.CharField(max_length=200)
  amount = models.IntegerField()