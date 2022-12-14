from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('home.html', views.home, name='contact'),
    path('contact', views.contact, name='contact')

    
]
