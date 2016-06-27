from django.conf.urls import include, url
from home import views

# Create your views here.
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^users/create', views.UserCreate.as_view(), name='create_user'),
    url(r'^home/login', views.UserLogin.as_view(), name='login'),
    url(r'^search',views.SearchForm.as_view(), name = 'search'),
    url(r'^quick_search',views.QuickSearch.as_view(), name = 'quick_search'),
    url(r'^broad_range',views.BroadSearch.as_view(), name = 'broad_range'),
    url(r'^markets',views.Markets.as_view(), name = 'markets'),
    url(r'^characteristic',views.Characteristic.as_view(), name = 'characteristic'),
    url(r'^users/logout', views.UserLogout.as_view(), name='logout'),
    url(r'^home', views.Home.as_view()),
    url(r'^home/created', views.Created.as_view(), name = 'created'),
    url(r'^bond_screen',views.ScreenBond.as_view(), name = 'bond_screen'),
    url(r'^moody_screen',views.Moodys.as_view(), name = 'moody_screen'),
    url(r'^merrill_screen',views.Merrill.as_view(), name = 'merrill_screen'),

]