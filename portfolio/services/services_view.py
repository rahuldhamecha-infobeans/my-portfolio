from django.views.generic import View,TemplateView,ListView
from portfolio.services.models import Service

class IndexView(ListView):
    template_name = 'portfolio/services.html'
    paginate_by = 6
    model = Service
    context_object_name = 'services'