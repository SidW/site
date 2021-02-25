from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    pages = ['polls', 'downloads', 'admin']
    return HttpResponse(render(request, 'landing.html',
                        {'pages': pages}))