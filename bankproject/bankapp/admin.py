from django.contrib import admin

# Register your models here.
from .models import district,branch,persondetails


admin.site.register(district)
admin.site.register(branch)
admin.site.register(persondetails)