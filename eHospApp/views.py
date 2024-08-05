from django.conf import settings
from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.mail import send_mail

# Create your views here.
default_data = {
    'appname': 'Ehospital App',
    'no_header_pages': ['signup_page','profile_page','signin_page','otp_page','book-appointment']
}
def index(request):
    default_data['current_page'] = 'signup_page'
    return render (request,"ehos_admin/signup_page.html",default_data)

def signin_page(request):
    default_data['current_page'] = 'signin_page'
    return render(request,"ehos_admin/signin_page.html",default_data)

def dashboard_page(request):
    default_data['current_page'] = 'dashboard_page'
    return render (request,"ehos_admin/dashboard_page.html",default_data)

def profile_page(request):
    default_data['current_page'] = 'profile_page'
    if 'email' not in request.session:
        return redirect(index)
    
    profile_data(request) # call profile_data methon to collect profile_data
    return render(request,"ehos_admin/profile_page.html",default_data)

def otp_page(request):
    default_data['current_page'] = 'otp_page'
    return render(request,"ehos_admin/otp_page.html",default_data)

def book(request):
    default_data['current_page'] = 'book-appointment'
    return render(request, "Main/book-appointment.html",default_data)

def signup(request):
     print(request.POST)
    
     request.session['reg_data'] = {
         'email' : request.POST['email'],
         'password' : request.POST['password'],
     }
     
     create_otp(request)
     return redirect(index)
   

# profile_image upload

def profile_image_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)
    
    profile.ProfileImage = request.FILES['profile_image']
    
    profile.save()
    return redirect(profile_page)

# for appointment

def appointment(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)
    appointment = Appointment.objects.get(Master = master)
    
    appointment.First_Name = request.POST['first_name']
    appointment.Last_Name = request.POST['last_name']
    appointment.Gender = request.POST['Gender']
    appointment.Service = request.POST['service']
    appointment.Date_Time = request.POST['date']
    appointment.Email = request.POST['email']
    appointment.Phone_no = request.POST['phone_number']
    
    dob = request.POST['dob'].split('-')
    appointment.DOB = '-'.join(dob)
    appointment.save() 
    
    return redirect(book-appointment)    

# profile_data
def profile_data(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)

    default_data['profile_data'] = profile
    
# profile_update

def profile_update(request):
    master = Master.objects.get(Email = request.session['email'])
    profile = Profile.objects.get(Master = master)
    
    profile.FullName = request.POST['full_name']
    profile.City = request.POST['city']
    profile.State = request.POST['state']
    profile.Gender = request.POST['gender']
    profile.Address = request.POST['address']
    profile.Pincode = request.POST['pincode']
    
    dob = request.POST['dob'].split('-')#.reverse()
    profile.DOB = '-'.join(dob)
    profile.save()      
    return redirect(profile_page)

# create OTP

def create_otp(request):
    email_to_list = [request.session['reg_data']['email'],]
    subject = "OTP varification for Ehospital"

    otp = randint(1000, 9999)

    print('OTP is: ', otp)

    request.session['otp'] = otp

    message = f"Your One Time Password for verification is: {otp}"

    email_from = settings.EMAIL_HOST_USER

    send_mail(subject, message, email_from, email_to_list)
    
# verification

def verify_otp(request):
    otp = int(request.POST['otp'])

    if otp == request.session['otp']:
        master = Master.objects.create(
            Email = request.session['reg_data']['email'],
            Password = request.session['reg_data']['password'],
            IsActive = True,
        )
        
        Profile.objects.create(
            Master = master,
        )

        del request.session['otp']
        del request.session['reg_data']

        print('otp verify success!')

        return redirect(signin_page)
    else:
        print('invalid otp')

    return redirect(index)


def registration(request):
    print(request.POST)

    request.session['reg_data'] = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }

    create_otp(request)

    return redirect(otp_page)
           
def login(request):
    print(request.POST)
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect (profile_page)
        else:
            print("Incollect Passowrd")
    except Master.DoesNotExist as err:
        print(err)
        return redirect(index)
    
    default_data['current_page'] = 'login'
    return redirect(index)

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(index)

