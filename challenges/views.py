from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.
def january():
    return HttpResponse("Eat no meat for the entire month!")
def february():
    return HttpResponse("Walk for at least 20 minutes every day!")

def march():
    return HttpResponse("Learn Django for al least 20 minutes every day!")

def monthly_challenge_by_number(request,month):
    return HttpResponse(month)


def monthly_challenge(request,month):
    challenge_text = None
    if(month=='january'):
        challenge_text= january()
    elif(month=='february'):
        challenge_text= february()
        
    elif(month=='march'):
        challenge_text= march()
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)