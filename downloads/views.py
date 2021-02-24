from django.shortcuts import render
from django.http import HttpResponse
from mysite import settings

import os


def index(request):
    resource_dir = settings.BASE_DIR.joinpath('resources/')

    return HttpResponse(render(request, 'downloads/index.html',
                               {'files': os.listdir(resource_dir),
                                'resource_dir': resource_dir}))


def test(request):
    return HttpResponse(render(request, 'test.html'))
