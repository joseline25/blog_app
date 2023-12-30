from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserProfileForm, UserForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')  
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

""" 
- The view checks if the request method is POST. If it is, 
the registration form is submitted, and the form data is processed.
- The `UserCreationForm` is instantiated with the POST data. If the 
form is valid, a new user is created and saved to the database using `form.save()`.
- The user is then logged in using `login(request, user)` 
to establish the user's session.
- Finally, the user is redirected to the home page.
"""

""" 
The profile view is responsible for displaying and updating the user profile. 
If the request method is POST, it processes the form data and saves the updated 
user and profile information. If the request method is GET, it retrieves the 
user and profile forms with the current user's data.

"""


@login_required
def profile(request):
    
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('authentication:profile')
        """ 
        It does not save the profile_form values but it saves the user_form values
        work on saving the profile pic and the biagraphy of the user
        """
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'current_user': request.user,
    }

    return render(request, 'authentication/profile.html', context)