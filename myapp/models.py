from django.db import models


class employees(models.Model):
    firstname=models.CharField(max_length=10,primary_key=True)
    lastname=models.CharField(max_length=10)
    empid=models.IntegerField()
    password=models.CharField(max_length=30,default="")
