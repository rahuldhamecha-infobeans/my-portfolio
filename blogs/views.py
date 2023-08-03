from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, resolve
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class IndexView(TemplateView):
    template_name = 'blogs/index.html'
