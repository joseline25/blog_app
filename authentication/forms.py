from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

# form to create a user profile
""" 
UserProfileForm is responsible for updating the profile-specific fields like
the profile picture and biography
"""

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'biography']


""" 
UserForm is used to update the user's general information such as first name,
last name, and email.
"""

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']