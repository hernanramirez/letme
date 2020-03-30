from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from .models import Parkings
#import mongoengine

class ListadoParkings(ListView):
    model = Parkings
    template_name = 'lista.html'
    context_object_name = 'Parkings'
    #queryset = Parkings.objects.filter(provider = 'parkimeter')

