from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    upperdawn = list('abcdefghijklmnopqrstuvwxyz')
    upperup = list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special = list('!@#$%^&*()')
    number = list('0123456789')

    PSWD = ''
    PSWD2 = ''
    PSWD3 = ''
    PSWD4 = ''
    PSWD5 = ''
    length = int(request.GET.get('length',10))
    for x in range(length):
        if request.GET.get("uppercase"):
            upperdawn.extend(upperup)
        if request.GET.get("special"):
            upperdawn.extend(special)
        if request.GET.get("numbers"):
            upperdawn.extend(number)
        PSWD += random.choice(upperdawn)
        PSWD2 += random.choice(upperdawn)
        PSWD3 += random.choice(upperdawn)
        PSWD4 += random.choice(upperdawn)
        PSWD5 += random.choice(upperdawn)

    return render(request, 'generator/password.html', { "PSWD": PSWD,"PSWD2": PSWD2,"PSWD3": PSWD3,"PSWD4": PSWD4,"PSWD5": PSWD5 })

def info(request):
    return render(request, 'generator/info.html')
