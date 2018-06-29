
import urls
from django.shortcuts import render
from django.http import HttpResponse

def WelcomePage(request):
    
    return render(request ,'reservation/welcome.html')