from django.urls import path
from . import views


urlpatterns = [
    path('<int:month>', views.monthly_challenge_int),
    path('<str:month>', views.monthly_challenge),
    path('sayhi/<str:name>/<int:age>', views.sayhi),
]
