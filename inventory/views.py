from django.shortcuts import render
from .models import distributor

def Show_distributor(request):

    distributors = distributor.Distributor.objects.all()
    ctx = {

        'distributors': distributors,
    }

    return render (request, 'distributor.html', ctx)
# Create your views here.
