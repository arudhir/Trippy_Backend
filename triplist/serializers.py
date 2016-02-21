from rest_framework.serializers import ModelSerializer
from triplist.models import triplist

class TriplistSerializer(ModelSerializer):
    class Meta:
        model = triplist