from django.urls import path, include
from . import views
app_name = "pages"


urlpatterns = [ 
    path('/', views.homepage, name="homepage"), 
    path('', views.homepage, name="homepage"),
    path('/home', views.appindex, name="site_home"),
    path('register', views.register, name="register"),
    path('site/login', views.login, name="site_login"),
    path('site/', include('django.contrib.auth.urls')), 
] 
