from django.conf.urls import url

from . import views

urlpatterns = [
  # /dashboard
  url('', views.home, name='home'),
]