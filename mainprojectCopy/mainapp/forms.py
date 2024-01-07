# mainapp/forms.py 

from django import forms
# to save username and password in the database
from .models import UserProfile
# for email and password handle
from django.contrib.auth.forms import AuthenticationForm # UserCreationForm
#for strong password 
from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User



#orignal: 
class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'confirm_password']
        widget = { 
            'password':forms.PasswordInput(),
        }

'''
#modified --
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']


'''   



# for email and password handle

class EmailAuthenticationForm(AuthenticationForm):
    def clean_username(self):
        return self.cleaned_data['username'].lower()





# for login check
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        # Check if the user exists in the database
        if not UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError('Invalid credentials. Please sign up first.')

        # Retrieve the user from the database
        user = UserProfile.objects.get(username=username)

        # Check if the provided password matches the stored password
        if not user.check_password(password):
            raise forms.ValidationError('Invalid credentials. Please sign up first.')

        # Log in the user
            login(self.request, user)

        return cleaned_data