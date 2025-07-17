from django.shortcuts import render,redirect
from .models import *
from authsystem.models import *

def home(request):
    username = request.session.get('username')
    if username:
        cust_obj=Customer.objects.filter(username=username)
        labour_obj=Labour.objects.all()
        return render(request,"customer/home.html",{'labour_obj':labour_obj,'cust_obj':cust_obj})
    else:
        return redirect("/authsystem/login_attempt/")