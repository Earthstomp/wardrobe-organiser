from django.urls import path
from .views import ClothingListAPIView

urlpatterns = [
    path('clothes', ClothingListAPIView.as_view(), name="clothes")
]
