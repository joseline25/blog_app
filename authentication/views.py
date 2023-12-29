from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
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


# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('blog:home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'authentication/login.html', {'form': form})