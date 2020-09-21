
from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = 'Travelkit'
admin.site.site_title = 'Welcome to the Travelkit'
admin.site.index_title = 'Welcome to this Portal'
urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('destinations/', views.destinations, name= "destinations")
]
