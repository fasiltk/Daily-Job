from django.shortcuts import render, redirect, get_object_or_404
from authsystem.models import *
from .models import *
from django.db.models import Prefetch
from datetime import datetime
from django.contrib import messages
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


def book(request, id):
    username = request.session.get('username')
    if not username:
        return redirect('/authsystem/login_attempt/')

    profession = get_object_or_404(Profession, id=id)
    labour = profession.labour

    try:
        customer = Customer.objects.get(username=username)
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found.")
        return redirect("/authsystem/login_attempt/")

    # 🔹 Get all booked dates for this labour
    booked_dates = Book.objects.filter(labour=labour).values_list('date', flat=True)

    if request.method == "POST":
        location_name = request.POST.get("location_name")
        b_address = request.POST.get("b_address")
        date_str = request.POST.get("date")

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect(request.path)

        if date in booked_dates:
            messages.error(request, "This labour is already booked on that date.")
            return redirect(request.path)

        Book.objects.create(
            labour=labour,
            cust_username=username,
            date=date,
            location_name=location_name,
            b_address=b_address
        )
        messages.success(request, "Booking successful!")
        return redirect("/customer/home/")

    return render(request, "customer/book.html", {
        "labour": labour,
        "profession": profession,
        "customer": customer,
        "booked_dates": booked_dates,  # 🔹 Pass to template
    })