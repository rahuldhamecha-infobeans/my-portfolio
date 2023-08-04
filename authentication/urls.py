from django.urls import path, re_path
from authentication import views,users_views,blog_views

app_name = 'auth'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path("logout/",views.LogoutView.as_view(),name='logout'),
    re_path(r'^register/?\w?',views.IndexView.as_view(),name='register'),
    path('my-account/',users_views.IndexView.as_view(),name='my_account'),
    path('blogs/',blog_views.IndexView.as_view(),name='blogs')
]
