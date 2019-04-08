from django.db import models

# Create your models here.
#model.py

from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateTimeField()
    salary = models.FloatField()
    photo = models.ImageField(upload_to='images/',default='download.jpg',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = "employees"
