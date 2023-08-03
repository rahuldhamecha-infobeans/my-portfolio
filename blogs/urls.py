from django.urls import path, re_path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index')
]
