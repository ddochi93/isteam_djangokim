from django.shortcuts import render

# Create your views here.
from viewer.models import Data


def hello(request):
    data = Data.objects.all()
    return render(request, 'hello.html', {
        'data': data
    })