from django.urls import path
from .views import RegisterTrainerAPIView, RegisterStudentAPIView, ProfileAPIView, LoginTrainerAPIView, LoginStudentAPIView

urlpatterns = [
    path('register/trainer/', RegisterTrainerAPIView.as_view(), name='register_trainer'),
    path('register/student/', RegisterStudentAPIView.as_view(), name='register_student'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('login/trainer/', LoginTrainerAPIView.as_view(), name='login_trainer'),
    path('login/student/', LoginStudentAPIView.as_view(), name='student_trainer'),
]
