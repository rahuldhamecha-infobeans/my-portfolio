from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class IndexView(TemplateView):
    template_name = 'blogs/index.html'
