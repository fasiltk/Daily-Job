from django.shortcuts import render,redirect
from .models import *
from customer.models import *
from authsystem.models import *

# def home(request):
#     username = request.session.get('username')
#     if not username:
#         return redirect('/authsystem/login_attempt/')  
#     book_data=Book.objects.filter(lab_username=username)
#     cust_user=Customer.objects.filter(username=book_data.customer.username)
#     return render(request,"labour/home.html",{"book_data":book_data})


def home(request):
    username = request.session.get('username')
    if not username:
        return redirect('/authsystem/login_attempt/')  

    # Load bookings and preload customer details
    book_data = Book.objects.filter(lab_username=username).select_related("customer")

    return render(request, "labour/home.html", {
        "book_data": book_data,
    })
