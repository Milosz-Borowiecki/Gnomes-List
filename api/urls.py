from django.urls import path
from .views import *

urlpatterns = [
    path('',GetGnome.as_view()),
    path('create',CreateGnome.as_view()),
    path('<int:pk>/',UpdateGnome.as_view()),
    path('delete/<int:pk>',DeleteGnome.as_view())
]