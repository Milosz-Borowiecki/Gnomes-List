from rest_framework import generics
from rest_framework import permissions
from .serializers import *
from .models import *

class CreateGnome(generics.CreateAPIView):  
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GetGnome(generics.ListAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer

class UpdateGnome(generics.RetrieveUpdateAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteGnome(generics.DestroyAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    permission_classes = [permissions.IsAuthenticated]