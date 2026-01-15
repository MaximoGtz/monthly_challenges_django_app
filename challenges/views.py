from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def monthly_challenge(request, month):
    message = None
    if month == 'jan':
        message = 'January'
    elif month == 'feb':
        message = 'February'
    elif month == 'mar':
        message = 'March'
    elif month == 'apr':
        message = 'April'
    else:
        return HttpResponseNotFound("Month is not available")
    return HttpResponse(message)


def monthly_challenge_int(request, month):
    message = None
    if month == 1:
        message = 'January'
    elif month == 2:
        message = 'February'
    elif month == 3:
        message = 'March'
    elif month == 4:
        message = 'April'
    else:
        return HttpResponseNotFound("Month is not availables")
    return HttpResponse(message)


def sayhi(request, name, age):
    return HttpResponse(f"Nice to meet you, {name}! You are {age} years old.")
