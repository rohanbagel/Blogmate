from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import ProfileModel  # Import your ProfileModel

def sign_up(request): 
    if request.method == 'POST': 
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Use get_or_create to avoid IntegrityError
            ProfileModel.objects.get_or_create(user=user)
            return redirect('users-login')  # Redirect to login after sign-up
    else:
        form = SignUpForm()
            
    context = {
        'form': form, 
    }
    return render(request, 'users/sign_up.html', context)


def profile(request):
    # Get or create the user's profile
    profile, created = ProfileModel.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form, 
        'profile': profile  # Optionally pass the profile to the template
    }
    return render(request, 'users/profile.html', context)
