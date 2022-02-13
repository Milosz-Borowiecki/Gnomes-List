from rest_framework import serializers
from api.models import Gnome

class GnomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gnome
        fields = '__all__'