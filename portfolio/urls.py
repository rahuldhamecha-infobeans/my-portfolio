from django.urls import path, re_path
from portfolio import views

app_name = 'portfolio'

urlpatterns = [
    re_path(r'^$',views.IndexView.as_view(),name='index'),
]
