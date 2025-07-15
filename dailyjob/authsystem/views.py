from django.shortcuts import render,redirect
from .models import *
import uuid
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"authsystem/index.html")

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        request.session['username']=username

        if role == 'customer':
            customer_obj = Customer.objects.filter(username=username,password=password).first()
            if customer_obj:
                if customer_obj.is_verified: 
                    return redirect('/customer/home/')
                else :
                    messages.error(request,'Account is not verified check your mail')
            else :
                messages.error(request,'Invalid Username or Password')
        else:
            labour_obj = Labour.objects.filter(username=username,password=password).first()
            if labour_obj:
                if labour_obj.is_verified :
                    return redirect('/labour/home/')
                else:
                    messages.error(request,'Account is not verified check your mail')
            else:
                messages.error(request,'Invalid Username or Password')

    return render(request,"authsystem/login.html")

def register_customer(request):
    alert_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        # image = request.FILES['image']
        image = request.FILES.get('image', None)

        auth_token = str(uuid.uuid4())
        customer_obj=Customer(username=username,password=password,name=name,phone_number=phone_number,address=address,auth_token=auth_token,image=image)
        exsist_customer = Customer.objects.filter(username=username).first()
        if exsist_customer:
            messages.error(request,'Username is already taken')
        else:
            customer_obj.save()
            alert_flag = True

        send_mail_after_registration(username,auth_token)


    return render(request,"authsystem/register_customer.html", {'alert_flag': alert_flag})


def register_labour(request):
    alert_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        profession = request.POST.get('profession')
        place = request.POST.get('place')
        fees = request.POST.get('fees')
        other_profession = request.POST.get('other_profession')
        image = request.FILES['image']  # Access the uploaded file

        auth_token = str(uuid.uuid4())
        exsist_labour = Labour.objects.filter(username=username).first()
        if exsist_labour:
            messages.error(request, "Username is already taken")
        else:
            # Check for 'other' profession and save the labour
            profession_to_save = other_profession if profession == 'other' else profession
            labour_obj = Labour(
                username=username,
                password=password,
                name=name,
                phone_number=phone_number,
                # profession=profession_to_save,
                place=place,
                fees=fees,
                image=image,  # Directly save the image field
                auth_token=auth_token
            )
            labour_obj.save()
            Profession.objects.create(labour=labour_obj, profession=profession_to_save)
            alert_flag = True
            send_mail_after_registration(username, auth_token)

    return render(request, "authsystem/register_labour.html", {'alert_flag': alert_flag})

def send_mail_after_registration(username, token):
    subject = 'Click the link for your account verification'
    message = f'Hi past the link to verify your account http://127.0.0.1:8000/authsystem/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [username]
    send_mail(subject,message,email_from,recipient_list)

def verify(request, auth_token):
    # Check for a profile in both Customer and Labour models
    profile_obj = Customer.objects.filter(auth_token=auth_token).first() or Labour.objects.filter(auth_token=auth_token).first()

    if profile_obj:
        profile_obj.is_verified = True
        profile_obj.save()
        # Redirect based on the type of profile (Customer or Labour)
        if isinstance(profile_obj, Customer):
            return redirect('customer')
        elif isinstance(profile_obj, Labour):
            return redirect('labour')
    else:
        messages.error(request, 'Invalid verification link')
        return redirect('index')







def a(request):
    return render(request,"authsystem/a.html")