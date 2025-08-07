from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Workout

# Create your views here.
def home(request):
    return render(request, 'index.html')

def workouts(request):
    workouts_list = Workout.objects.all()
    return render(request, "workouts.html", {"workouts": workouts_list})