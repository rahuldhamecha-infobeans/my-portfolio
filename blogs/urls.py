from django.urls import path, re_path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    re_path(r"^(?P<pk>\d+)/(?P<name>[\w-]+)/$", views.BlogDetailView.as_view(),name='blog_details'),
]
