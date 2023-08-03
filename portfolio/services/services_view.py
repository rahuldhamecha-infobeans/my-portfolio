from django.views.generic import View,TemplateView,ListView
from portfolio.services.models import Service

class IndexView(ListView):
    template_name = 'portfolio/services.html'
    paginate_by = 6
    model = Service
    context_object_name = 'services'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['services'] = self.get_services()
    #     return context
    #
    # def get_services(self):
    #     services = Service.objects.order_by('id')
    #     return services