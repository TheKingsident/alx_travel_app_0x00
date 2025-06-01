from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer
from django.http import JsonResponse


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

def index(request):
    return JsonResponse({'message': 'Hello from listings!'})