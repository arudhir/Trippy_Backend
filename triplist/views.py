from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse
from .models import TripList
#from rest_framework.viewsets import ModelViewSet
#from triplist.serializers import TriplistSerializer

# Create your views here.
# 
def home(request):
    return render_to_response("Triplist/home.html", {'TripList': TripList.objects.all()})

#class TripViewSet(ModelViewSet):
#    queryset = TripList.objects.all()
#    serializer_class = TriplistSerializer