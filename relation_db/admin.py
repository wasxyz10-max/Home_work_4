from django.contrib import admin
from . import models 


admin.site.register(models.Person)
admin.site.register(models.TourPerson)
admin.site.register(models.Type)
admin.site.register(models.ReviewPerson)