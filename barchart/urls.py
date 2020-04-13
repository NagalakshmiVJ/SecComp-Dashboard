from django.conf.urls import url

from . import views

urlpatterns = [
  # /barchart
  url('', views.home, name='home'),
]