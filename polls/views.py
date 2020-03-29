from django.shortcuts import render
from django.http import HttpResponse
"""
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
"""

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")