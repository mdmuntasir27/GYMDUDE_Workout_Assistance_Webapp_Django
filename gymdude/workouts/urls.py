from django.urls import path
from . import views

#paths will be written here
urlpatterns = [
    path("test/", views.test_text, name="test")
]