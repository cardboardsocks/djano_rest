from django.shortcuts import render

from rest_framework import viewsets

from api.serializers import ShoeSerializer

from shoestore.models import Shoe


# Create your views here.
class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer