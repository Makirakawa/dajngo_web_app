from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    return HttpResponse("етстировка старницы test")

def main_window(request):
    return HttpResponse("[main_window] станица ")

def window_two(request):
    return HttpResponse("[main_window] --> [window_two] станица ")

def window_three(request):
    return HttpResponse("[main_window] --> [window_three] станица ")
