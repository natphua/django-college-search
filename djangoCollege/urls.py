from django.contrib import admin
from django.urls import path
from collegeStats.views import result, get_college

# attaches a view to a certain url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_college, name='home'),
    path('result/', result),
]
