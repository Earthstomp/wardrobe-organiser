from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Clothing
from .serializers import ClothingSerializer


class ClothingListAPIView(generics.ListAPIView):

    serializer_class = ClothingSerializer

    def get_queryset(self):
        return Clothing.objects.all()


class ClothingDetailAPIView(generics.ListAPIView):
    serializer_class = ClothingSerializer

    def get(self, request, slug):
        query_set = Clothing.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)
