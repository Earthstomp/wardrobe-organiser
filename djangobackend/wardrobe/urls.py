from django.urls import path
from .views import ClothingListAPIView, ClothingDetailAPIView

urlpatterns = [
    path('clothes', ClothingListAPIView.as_view(), name="clothes"),
    path('clothes/<str:slug>', ClothingDetailAPIView.as_view(), name="clothing")
]
