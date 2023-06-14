from django.shortcuts import render
from rest_framework import generics
from .models import Clothing
from .serializers import ClothingSerializer


class ClothingListAPIView(generics.ListAPIView):

    serializer_class = ClothingSerializer

    def get_queryset(self):
        return Clothing.objects.all()
