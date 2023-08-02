from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

class ContactView(TemplateView):
    template_name = 'portfolio/contact_us.html'