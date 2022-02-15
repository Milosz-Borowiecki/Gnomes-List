from rest_framework import generics
from rest_framework import permissions
from django_filters import rest_framework as filters
from .serializers import *
from .models import *

class CreateGnome(generics.CreateAPIView):  
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GnomeFilter(filters.FilterSet):

    race_enum = filters.ChoiceFilter(field_name="race")

    class Meta:
        model = Gnome
        fields = ['race']

class GetGnome(generics.ListAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GnomeFilter

class UpdateGnome(generics.RetrieveUpdateAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteGnome(generics.DestroyAPIView):
    queryset = Gnome.objects.all()
    serializer_class = GnomeSerializer
    permission_classes = [permissions.IsAuthenticated]
