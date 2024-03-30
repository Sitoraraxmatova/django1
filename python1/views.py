from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    return HttpResponse('salom dunyo')


def content(request):
    return HttpResponse('content')
def rain(request):
    return HttpResponse('rain')
def rais(request):
    return HttpResponse('rais')