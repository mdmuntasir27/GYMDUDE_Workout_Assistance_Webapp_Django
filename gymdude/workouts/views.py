from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def test_text(request):
    return HttpResponse("I love you!")