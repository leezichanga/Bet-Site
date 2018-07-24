from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
# from django.template import RequestContext
# from django.contrib.auth import authenticate,login
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login')
def home(request):
    return render(request, 'index.html')
