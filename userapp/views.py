from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from.models import Profile
from.serializers import UserSerializer, ProfileSerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

