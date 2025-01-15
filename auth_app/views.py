from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser, Profile
from .serializers import (RegisterTrainerSerializer, RegisterStudentSerializer,
                          ProfileSerializer, LoginTrainerSerializer,LoginStudentSerializer)


class RegisterTrainerAPIView(APIView):
    def post(self, request):
        serializer = RegisterTrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Trainer registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginTrainerAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_trainer:
                # Trainer login successful
                return Response({"message": f"Trainer {user.first_name} has successfully logged in."}, status=status.HTTP_200_OK)
            else:
                # User exists but is not a trainer
                return Response({"detail": "No Trainer Account with the provided credentials Found."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Invalid credentials
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

class RegisterStudentAPIView(APIView):
    def post(self, request):
        serializer = RegisterStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_OK)

class LoginStudentAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_student:
                # Student login successful
                return Response({"message": f"Student {user.first_name} has successfully logged in."}, status=status.HTTP_200_OK)
            else:
                # User exists but is not a student
                return Response({"detail": "No Student Account with the provided credentials Found."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Invalid credentials
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
