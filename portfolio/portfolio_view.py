from django.views.generic import View, TemplateView, ListView
from portfolio.models import Portfolio


class IndexView(ListView):
    template_name = 'portfolio/portfolio.html'
    paginate_by = 9
    model = Portfolio
    context_object_name = 'portfolio_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = self.get_portfolios(context['page_obj'].object_list)
        return context

    def get_portfolios(self,portfolios):
        # portfolios = Portfolio.objects.order_by('name')
        categories = set()
        for portfolio in portfolios:
            categories.add(portfolio.category.name)

        return {'portfolios': portfolios, 'portfolio_categories': categories}