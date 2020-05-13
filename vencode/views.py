from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, "home.html",
                  {'date': datetime.now().year})


def index(request):
    return HttpResponse("Under construction!")
