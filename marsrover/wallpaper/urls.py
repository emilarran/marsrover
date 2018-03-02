from django.conf.urls import url
from . import views
from .views import HomeView, Something

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='homepage'),
    url(r'^get-image/$', Something.as_view(), name='homepage'),
    # url(r'^$', views.homepage, name='homepage'),
]
