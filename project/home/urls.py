from django.conf.urls import include, url
from home import views

# Create your views here.
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^users/create', views.UserCreate.as_view(), name='create_user'),
    url(r'^home/login', views.UserLogin.as_view(), name='login'),
    url(r'^users/logout', views.UserLogout.as_view(), name='logout'),
    url(r'^home', views.Home.as_view())
]