from rest_framework import serializers
from .models import UserProfile, Website

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'full_name', 'profile_pic')

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('author', 'title', 'description', 'country', 'landing_page', 'uploaded_on')        