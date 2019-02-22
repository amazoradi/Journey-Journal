from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext
from django.urls import reverse
from Journal.models import *




def landing_page(request):
    """Renders main landing page for Journal 

    Model:None

    Template:index.html

    """
    return render(request, 'index.html')

