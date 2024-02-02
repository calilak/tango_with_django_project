from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'), #urls are mapped to the index view
    path('about/', views.about, name = 'about'),
    path('admin/', admin.site.urls),
]