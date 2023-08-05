from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from portfolio.services.models import Service
from portfolio.models import Portfolio, Testimonial
from blogs.models import Category,Blog


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.get_services()
        context['portfolio'] = self.get_portfolios()
        context['blog_categories'] = self.get_blogs_categories()
        context['recent_blogs'] = self.get_blogs()
        context['testimonials'] = self.get_testimonials()
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

    def get_blogs_categories(self,limit=4):
        categories = []
        category = Category.objects.order_by('name')
        for cat in category:
            if len(cat.blog_set.all()) > 0:
                categories.append(cat)

        if len(categories) > 4:
            categories = categories[:limit]

        return categories

    def get_testimonials(self):
        testimonials = Testimonial.objects.order_by('-id')
        return testimonials

    def get_blogs(self):
        blogs = Blog.objects.filter(status=True).order_by('id')

        if len(blogs) > 3:
            blogs = blogs[:3]

        return blogs



class ContactView(TemplateView):
    template_name = 'portfolio/contact_us.html'
