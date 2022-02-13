from rest_framework import serializers
from base.models import Gnome

class GnomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gnome
        fields = '__all__'