from django.views.generic import (View, TemplateView, ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blogs.forms import BlogForm
from blogs.models import Blog,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages

class IndexView(LoginRequiredMixin,ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'blogs'
    model = Blog
    paginate_by = 5

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Blog.objects.filter(
            user_id=self.request.user
        ).order_by('-date')


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    form_class = BlogForm
    # fields = ("title", "date", "content", "categories", "status", "blog_image")
    template_name = 'blogs/blog_add_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user)
        context['user_id'] = user.id or 0
        if 'is_error' in self.request.session and self.request.session['is_error']:
            context['is_error'] = True
            self.request.session['is_error'] = False
        else:
            context['is_error'] = False
        return context

    def get_success_url(self):
        return reverse_lazy('auth:blogs')

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        form.instance.user_id = user.id
        messages.success(self.request,'Blog Created Successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = '<ul>'
        error_data = form.errors.as_data()
        for error in error_data:
            errors += '<li>'+error_data[error][0].message+'</li>'

        errors += '</ul>'

        messages.error(self.request, errors)
        self.request.session['is_error'] = True
        return super().form_invalid(form)


class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogs/blog_add_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user)
        context['user_id'] = user.id or 0
        if 'is_error' in self.request.session and self.request.session['is_error']:
            context['is_error'] = True
            self.request.session['is_error'] = False
        else:
            context['is_error'] = False
        return context

    def get_success_url(self):
        return reverse_lazy('auth:blogs')

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        form.instance.user_id = user.id
        messages.success(self.request,'Blog Updated Successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = '<ul>'
        error_data = form.errors.as_data()
        for error in error_data:
            errors += '<li>'+error_data[error][0].message+'</li>'

        errors += '</ul>'

        messages.error(self.request, errors)
        self.request.session['is_error'] = True
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin,DeleteView):
    context_object_name = 'blog'
    model = Blog
    template_name = 'blogs/confirm_delete.html'
    success_url = reverse_lazy('auth:blogs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Delete Blog'
        return context