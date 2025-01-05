from django.contrib import admin
from django.urls import path, include
from myapp import views  # Add this line to import your views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Use the imported views.index here
]