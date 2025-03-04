from django.shortcuts import render,redirect
from django.urls import path
from .views import *
from .models import *
from django.conf import settings
import os

# profile image upload
def upload_image(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    image = request.FILES['avatar']
    
    image_name = image.name
    image_path = os.path.join(settings.MEDIA_ROOT, 'images/users')
    images = os.listdir(image_path)

    image_extension = image_name.split('.')[-1]

    new_image_name = f"{profile.id}_{master.Email.split('@')[0]}.{image_extension}"
    image.name = new_image_name

    
    print('image name:', image_name)
    print('new name:', new_image_name)
    print('image path:', images)

    if new_image_name in images:
        os.remove(os.path.join(image_path, new_image_name))

    profile.Avatar = image

    profile.save()

    return redirect(profile_page)