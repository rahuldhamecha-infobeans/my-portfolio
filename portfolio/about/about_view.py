from django.views.generic import View,TemplateView,ListView
from portfolio.models import Testimonial

class IndexView(TemplateView):
    template_name = 'portfolio/about.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = self.get_testimonials()
        return context

    def get_testimonials(self):
        testimonials = Testimonial.objects.order_by('-id')
        return testimonials