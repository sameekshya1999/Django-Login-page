# mainapp/urls.py
#signup is create new account
from django.urls import path
from .views import home, sign_up, login, forget_password ,CustomLoginView, sign_in, signin_error, upload_image

urlpatterns = [
    path('', home, name='home'),
    path('sign_up/',sign_up,name='sign_up'),
    path('login/',login, name='login'),
    path('forget_password/',forget_password, name='forget_password'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('sign_in/',sign_in,name='sign_in'),
    path('signin_error/',signin_error,name='signin_error'),
    path('upload_image/', upload_image, name='upload_image'),
    
]
