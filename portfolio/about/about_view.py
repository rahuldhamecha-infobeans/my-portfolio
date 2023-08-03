from django.views.generic import View,TemplateView,ListView
from portfolio.services.models import Service

class IndexView(TemplateView):
    template_name = 'portfolio/about.html'