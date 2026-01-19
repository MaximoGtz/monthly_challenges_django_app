from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

monthly_challenges = {
    "january": 'The first month of the year',
    "february": 'The second month of the year',
    "march": 'The third month of the year',
    "april": 'The fourth month of the year',
    "may": 'The fifth month of the year',
    "june": 'The sixth month of the year',
    "july": 'The seventh month of the year',
    "august": 'The eighth month of the year',
    "september": 'The next month of the year',
    "october": 'The first month of the year',
    "november": 'The second month of the year',
    "december": 'The third month of the year',
}


# Create your views here.
def monthly_challenge(request, month):
    challenge_text = monthly_challenges[month]
    if not challenge_text:
        return HttpResponseNotFound()
    else:
        return HttpResponse(challenge_text)


def monthly_challenge_int(request, month):
    months_list = list(monthly_challenges.values())
    challenge_text = months_list[month]
    if not challenge_text:
        return HttpResponseNotFound()
    else:
        return HttpResponse(challenge_text)


def sayhi(request, name, age):
    return HttpResponse(f"Nice to meet you, {name}! You are {age} years old.")
