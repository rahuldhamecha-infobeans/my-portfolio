from django.shortcuts import render
from authentication.forms import UserProfileForm, UserForm, LoginForm
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView,RedirectView)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, resolve
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = 'authentication/register.html'
    user_form = UserForm()
    profile_form = UserProfileForm()
    is_registered = False
    is_error = False

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            self.user_form = UserForm(data=request.POST)
            self.profile_form = UserProfileForm(data=request.POST)

            if self.user_form.is_valid() and self.profile_form.is_valid():
                user = self.user_form.save()
                user.set_password(self.user_form.cleaned_data['password'])
                user.save()

                profile = self.profile_form.save(commit=False)
                profile.user = user

                if 'profile_pic' in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']

                profile.save()
                self.is_registered = True
            else:
                self.is_error = True
                print(self.user_form.errors, self.profile_form.errors)
        return HttpResponseRedirect(reverse('auth:login'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.user_form
        context['profile_form'] = self.profile_form
        context['is_registered'] = self.is_registered
        context['is_error'] = self.is_error
        return context


class LoginView(View):
    login_form = LoginForm()
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('portfolio:index'))
        context = {
            'login_form' : self.login_form
        }
        return render(request, 'authentication/login.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = self.login_form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':

            self.login_form = LoginForm(data=request.POST)

            if self.login_form.is_valid():
                login_data = self.login_form.cleaned_data
                user = authenticate(username=login_data['username'],password=login_data['password'])
                login(request,user)
                return HttpResponseRedirect(reverse('portfolio:index'))
            else:
                context = {
                    'is_error': True,
                    'errors': self.login_form['username'].errors,
                    'login_form': self.login_form
                }
                return render(request, 'authentication/login.html', context)

class LogoutView(View):

    def get(self,request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('auth:login'))