from django.contrib import admin
from django.urls import path
from calcolo_stipendio import views

urlpatterns = [
    path('', views.salary_view, name='calcola_stipendio'),
    path('admin/', admin.site.urls),
]
