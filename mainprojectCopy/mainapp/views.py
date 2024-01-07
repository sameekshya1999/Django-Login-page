from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages framework
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse  # Import HttpResponse
from .forms import EmailAuthenticationForm, SignUpForm, LoginForm
from .models import UserProfile, UploadedImage
from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as auth_login


def home(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'login.html'

'''

def sign_in(request):
    return render(request, 'sign_in.html')

'''

def login(request):
    return render(request, 'login.html')


def forget_password(request):
    return render(request, 'forget_password.html')


def sign_up(request):
    return render(request, 'sign_in.html')





#for sigin in error
def signin_error(request):
   # return HttpResponse("Your account is already existed")
    return render(request, 'signin_error.html')



#### flg for login if user is not new --original

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is active and the flag is True
            if user.is_active and getattr(user, 'flag', False):
                # Flag is True and user is active, allow login
                login(request, user)
                return redirect('dashboard')
            elif not user.is_active:
                # User is not active, show a message or handle accordingly
                messages.error(request, 'Account is not active.')
            else:
                # Flag is False, show a message or handle accordingly
                messages.error(request, 'Account not allowed to log in.')
        else:
            # Authentication failed, show a message or handle accordingly
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

 



# Sign-in function with flag --modified
def sign_in(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']

            # Check if the username already exists in the database
            if User.objects.filter(username=username).exists():
                # Redirect the user to the 'signin_error' page
                messages.error(request, 'Account already exists. Please log in.')
                return redirect('signin_error')

            # Create a new user
            user = User(username=username)
            user.set_password(raw_password)
            user.save()

            # Create a corresponding UserProfile with the flag attribute
            user_profile = UserProfile(user=user, flag=True)
            user_profile.save()

            # Authenticate and log in the user
            authenticated_user = authenticate(request, username=username, password=raw_password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                # Redirect the user to the 'dashboard' page after login
                return redirect('dashboard')
            else:
                # Handle the case where authentication fails (unlikely)
                messages.error(request, 'Invalid username or password. Please try again.')
                return redirect('login')

    else:
        form = SignUpForm()

    return render(request, 'sign_in.html', {'form': form})


# Login function with flag check --modofied

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is active and the flag is True
            if user.is_active and getattr(user, 'flag', False):
                # Flag is True and user is active, allow login
                login(request, user)
                return redirect('dashboard')
            elif not user.is_active:
                # User is not active, show a message or handle accordingly
                messages.error(request, 'Account is not active.')
            else:
                # Flag is False, show a message or handle accordingly
                messages.error(request, 'Account not allowed to log in.')
        else:
            # Authentication failed, show a message or handle accordingly
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
    



def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST.get('description')

        uploaded_image = UploadedImage(image=image, description=description)
        uploaded_image.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})