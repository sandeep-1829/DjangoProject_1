from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def message(request):
    return HttpResponse('<h1>Question : Good Morning Sanju...!!!</h1>')


def answer(request):
    return HttpResponse ('<h1 class="bg-info"><marquee>Answer : I am Fine..How Do You Do...???</h3></marquee>')
