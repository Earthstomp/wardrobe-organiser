from django.shortcuts import render
from rest_framework import generics
from .models import Clothing


class ClothingListAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Clothing.objects.all()
