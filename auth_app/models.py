from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)
    invitation_code = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        # Automatically set username to first_name if not provided
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username or self.email

def validate_file_type(value):
    allowed_types = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ]
    if value.file.content_type not in allowed_types:
        raise ValidationError('Invalid file type. Only PDF or Word documents are allowed.')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone_number = PhoneNumberField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    birth_date = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=255, blank=True)
    linkedin_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    uploaded_cv = models.FileField(upload_to='cv_uploads/', validators=[validate_file_type])

    def __str__(self):
        return self.user.username


class InvitationCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
