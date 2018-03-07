from django.shortcuts import render
from dataapp.models import Content
# Create your views here.


def home(request):
    page_title = "Machine Healthcare"
    contents = Content.objects.get(page='home', title='first_title')
    return render(request, 'home/home.html', locals())
