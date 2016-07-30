from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.Landing, name='Landing'),
    url(r'register$', views.Register, name='Register'),
]