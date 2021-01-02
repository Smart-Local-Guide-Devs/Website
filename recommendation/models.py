from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Service(models.Model):
	serviceNo=models.AutoField(primary_key=True)
	serviceType=models.CharField(max_length=100)
	serviceName=models.CharField(max_length=100)
	slug=models.CharField(max_length=200)


	def __str__(self):
		return self.serviceName