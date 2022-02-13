from rest_framework import generics
from rest_framework import permissions
from .serializers import *
from .models import *

class CreateGnome(generics.CreateAPIView):  
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    
class GetGnome(generics.ListAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer

class UpdateGnome(generics.RetrieveUpdateAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer

class DeleteGnome(generics.DestroyAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer