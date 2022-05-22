from django.db import models

# Create your models here.
exp=[('1','1 year'),('2','2 year'),('3','3 year'),('+4','More than 4 year')]
class mentord(models.Model):
    name=models.CharField('Fullname of mentor',max_length=100)
    subject=models.CharField(max_length=100)
    experiance=models.CharField(max_length=50,choices=exp)
    contact=models.CharField(max_length=50)
    email=models.EmailField(null=True,help_text='The email id should contain @')
    def __str__(self):
        return self.name