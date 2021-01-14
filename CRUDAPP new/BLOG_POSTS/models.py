from django.db import models

# Create your models here.
class modelclass(models.Model):
    name=models.CharField(max_length=30)
    content=models.TextField(blank=True,null=True)
    rating=models.DecimalField(decimal_places=2,max_digits=3)
    def __str__(self):
        return self.name
