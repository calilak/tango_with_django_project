from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'), #urls are mapped to the index view
    path('about/', views.about, name = 'about'),
    path('category/<slug:category_name_slug>/', views.show_category,
          name='show_category'), #url mapping to the show_category view
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('admin/', admin.site.urls),
]