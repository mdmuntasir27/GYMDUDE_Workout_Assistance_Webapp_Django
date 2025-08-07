from django.forms import ModelForm
from .models import Workout

class WorkoutsForm(ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"