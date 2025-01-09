from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    class Category(models.TextChoices):
        Student = 'STU' , 'Student',
        Administration = 'ADM' , 'Administration',

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_picture = CloudinaryField('profile_pictures', blank=True, null=True)
    company_code = models.CharField(max_length=100)
    category = models.CharField(choices=Category.choices, default=Category.Student, max_length=100)

    def __str__(self):
        return f"{self.user.username} Profile"
