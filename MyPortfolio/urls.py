from django.urls import path
from .views import home , about , contact, project

urlpatterns = [
    path('', home, name= "home"),
    path('about/', about, name= "about" ),
    path('contact/', contact, name="contact"),
    path('project/', project, name="project"),
]