# from django.shortcuts import render,redirect
# from .models import *
# from authsystem.models import *

# def home(request):
#     username = request.session.get('username')
#     if username:
#         cust_obj=Customer.objects.filter(username=username)
#         labour_obj=Labour.objects.select_related('labour').all()
#         return render(request,"customer/home.html",{'labour_obj':labour_obj,'cust_obj':cust_obj})
#     else:
#         return redirect("/authsystem/login_attempt/")
    
from django.shortcuts import render, redirect
from authsystem.models import *
from .models import *
from django.db.models import Prefetch

def home(request):
    username = request.session.get('username')
    if not username:
        return redirect("/authsystem/login_attempt/")
    
    cust_obj = Customer.objects.filter(username=username)
    
    # Get all professions with labour preloaded
    profession_obj = Profession.objects.select_related('labour').all()
    
    return render(request, "customer/home.html", {
        'cust_obj': cust_obj,
        'profession_obj': profession_obj,
    })
