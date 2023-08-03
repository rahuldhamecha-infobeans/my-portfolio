from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from portfolio.services.models import Service

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.get_services()
        return context

    def get_services(self):
        services = Service.objects.order_by('id')[:6]
        return services

class ContactView(TemplateView):
    template_name = 'portfolio/contact_us.html'
