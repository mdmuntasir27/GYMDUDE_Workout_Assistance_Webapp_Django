from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Workout

# Create your views here.
def home(request):
    return render(request, 'index.html')

def workouts(request):
    workouts_list = Workout.objects.all()
    return render(request, "workouts.html", {"workouts": workouts_list})

def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    return render(request, 'workout_detail.html', {'workout': workout})