from django.urls import path
from .views import RegisterTrainerAPIView, RegisterStudentAPIView, ProfileAPIView

urlpatterns = [
    path('register/trainer/', RegisterTrainerAPIView.as_view(), name='register_trainer'),
    path('register/student/', RegisterStudentAPIView.as_view(), name='register_student'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
