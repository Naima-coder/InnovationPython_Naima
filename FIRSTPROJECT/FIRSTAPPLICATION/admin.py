from django.contrib import admin
from .models import student
from .models import trainer
from .models import recruiter
# Register your models here.
admin.site.register(student)
admin.site.register(trainer)
admin.site.register(recruiter)
