from django.urls import path
from . import views

#paths will be written here
urlpatterns = [
    path("", views.home, name="home"),
    path("workouts/", views.workouts, name="workouts"),
    path("workouts/<int:workout_id>/", views.workout_detail, name="workout_detail"),
]