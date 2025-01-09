from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import (ProfileListCreateView,ProfileDetailView)

urlpatterns = [
    # Profile API
    path('api/profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('api/profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
