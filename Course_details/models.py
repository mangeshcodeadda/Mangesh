from django.db import models

# Create your models here.
class CourseDetails(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    year = models.CharField(max_length=100,blank=True,null=True)
    branch = models.CharField(max_length=100,blank=True,null=True)

