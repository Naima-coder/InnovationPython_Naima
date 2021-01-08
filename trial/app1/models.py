from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    feedback=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
