from django.contrib import admin
from .models import College

# makes model data acccessible on admin site
admin.site.register(College)

