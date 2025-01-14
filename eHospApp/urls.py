from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('dashboard_page/',dashboard_page,name='dashboard_page'),
    path('profile_page/',profile_page,name='profile_page'),
    path('otp_page/',otp_page,name='otp_page'),
    path('book-appointment/',book,name='book-appointment'),
    path('appointment/',appointment,name='appointment'),
    path('profile_update/',profile_update,name='profile_update'),
    path('profile_image_upload/',profile_image_upload,name='profile_image_upload'),
    path('signin_page/',signin_page,name='signin_page'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',signup,name='signup'),    
]