from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from portfolio.services.models import Service
from portfolio.models import Portfolio, PortfolioCategory


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.get_services()
        context['portfolio'] = self.get_portfolios()
        return context

    def get_services(self):
        services = Service.objects.order_by('id')[:6]
        return services

    def get_portfolios(self):
        portfolios = Portfolio.objects.order_by('name')
        categories = set()
        for portfolio in portfolios:
            categories.add(portfolio.category.name)

        return {'portfolios': portfolios, 'portfolio_categories': categories}


class ContactView(TemplateView):
    template_name = 'portfolio/contact_us.html'
