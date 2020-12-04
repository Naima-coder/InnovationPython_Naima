from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class trainer(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class recruiter(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name