from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
   path('output/',Output.as_view(),name='output')
]
