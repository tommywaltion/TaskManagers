from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Login successfull! Welcome back")
            messages.get_messages(request).used = True  # Mark all messages as "read"
            return redirect('task_list')
        else:
            messages.error(request, 'invalid username or password')
            return render(request, 'Profile/login.html')

    return render(request, 'Profile/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Password do not match")
            return render(request, 'Profile/register.html')
        
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist")
            return render(request, 'Profile/register.html')

        try:
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return render(request, 'Profile/register.html')
        
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        login(request, user)
        # messages.success(request, "Registration Successful!, you are now logged in")
        messages.get_messages(request).used = True  # Mark all messages as "read"
        return redirect('login')

    return render(request, 'Profile/register.html')

def landing_page(request):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    return render(request, 'landing_page.html')

@login_required
def view_profile(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    messages.get_messages(request).used = True  # Mark all messages as "read"
    return render(request, 'Profile/view_profile.html', context)

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileUpdateForm(instance=profile)

    context = {
        'form': form
    }
    messages.get_messages(request).used = True  # Mark all messages as "read"
    return render(request, 'Profile/edit_profile.html', context)

def about_page(request):
    messages.get_messages(request).used = True  # Mark all messages as "read"
    return render(request, 'about_page.html')