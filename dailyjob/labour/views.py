from django.shortcuts import render,redirect,get_object_or_404
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

def approve(request,id):
    approve=get_object_or_404(Book,id=id)
    approve.confirm=True
    approve.save()
    return redirect('home')

def delete(request,id):
    delete=get_object_or_404(Book,id=id)
    delete.delete()
    return redirect('home')