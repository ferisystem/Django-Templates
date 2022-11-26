"""
To render html web pages
"""
from django.http import HttpResponse
import random


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    number = random.randint(11, 666)
    name = "Alireza"
    H1_STRING = f"""
    <h1>Hello {name} - {number}!</h1>
    """
    P_STRING = f"""
    <p>Hi {name} - {number}!</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)