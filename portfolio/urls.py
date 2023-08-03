from django.urls import path, re_path
from portfolio import views
from portfolio.services import services_view
from portfolio.about import about_view

app_name = 'portfolio'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('services/',services_view.IndexView.as_view(),name='services'),
    path('about/',about_view.IndexView.as_view(),name='about'),
]
