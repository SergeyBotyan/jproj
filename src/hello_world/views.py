from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time

# Create your views here.
def hello_world(request):
    return HttpResponse(f'Hello world! Now is {datetime.now()}')
