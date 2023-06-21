from django.db import models
from datetime import datetime


# Create your models here.
class MissingPersons(models.Model):
	date_missing = models.DateField(blank=True, default=datetime.now())
	last_name = models.CharField(max_length=25)
	first_name = models.CharField(max_length=25)
	age_at_missing = models.IntegerField(default=0)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=2)
	gender = models.CharField(max_length=1)
	race = models.CharField(max_length=1)
	
