
from django.http import HttpResponse

from datetime import datetime


def hello_world(request):
   
    return HttpResponse('Hello, world!, Current server time is {now}'.format(
        now=str(datetime.now().strftime('%b %dth, - %H:%M hrs'))))


def hi(request):
    
    return HttpResponse('Hi!')