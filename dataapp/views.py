from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/home.html', locals())

def others(request):
    return render(request, 'others/others.html', locals())