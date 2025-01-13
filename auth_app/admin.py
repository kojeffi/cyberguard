from django.contrib import admin
from .models import InvitationCode, Profile, CustomUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'gender', 'birth_date', 'education', 'linkedin_url')
    search_fields = ('user__username', 'phone_number', 'education')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_trainer', 'is_student', 'invitation_code')
    search_fields = ('username', 'email')
    list_filter = ('is_trainer', 'is_student')


@admin.register(InvitationCode)
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'used_by')  # Ensure these fields exist in InvitationCode model
    search_fields = ('code',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
