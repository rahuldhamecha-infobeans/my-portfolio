from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, resolve
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from blogs.models import Blog,Category


class IndexView(ListView):
    template_name = 'portfolio/blogs.html'
    model = Blog
    context_object_name = 'blogs'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_cats'] = self.get_all_categories()
        search_cat = self.request.GET.get('search_cat')
        search_title = self.request.GET.get('search_title')
        if search_title:
            context['search_title'] = search_title
        if search_cat:
            context['blogs_cat'] = search_cat
        return context

    def get_queryset(self):
        blogs = super().get_queryset()
        search_title = self.request.GET.get('search_title')
        search_cat = self.request.GET.get('search_cat')
        blogs = blogs.filter(status=True)
        if search_title:
            blogs = blogs.filter(title__contains=search_title)

        if search_cat:
            blogs = blogs.filter(categories__name__startswith=search_cat)
        return blogs

    def get_all_categories(self):
        categories = Category.objects.all()
        return categories


class BlogDetailView(DetailView):
    template_name = 'portfolio/blog_details.html'
    model = Blog
    context_object_name = 'blog_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_detail = context['blog_detail']
        categories = blog_detail.categories.all()
        context['categories'] = categories
        context['all_cats'] = self.get_all_categories()
        context['recent_blogs'] = self.get_recent_blogs()

        return context

    def get_all_categories(self):
        categories = Category.objects.all()
        return categories

    def get_recent_blogs(self):
        context = super().get_context_data()
        blog_detail = context['blog_detail']
        categories = blog_detail.categories.all()
        cat_ids = []
        for cat in categories:
            cat_ids.append(cat.id)
        blogs = Blog.objects.filter(categories__in=cat_ids).order_by('-id').exclude(pk=blog_detail.pk)
        if len(blogs) > 5:
            blogs = blogs[:5]

        return blogs