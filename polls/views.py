from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template import loader
# Create your views here.
def index(request):
   template =loader.get_template('polls/index.html');
   return render(request,'polls/index.html');
