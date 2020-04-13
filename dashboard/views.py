# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def initialize_context(request):
  context = {}

  return context


def home(request):
  context = initialize_context(request)

  return render(request, 'dashboard/home.html', context)