from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from customer.models import *
from authsystem.models import *

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


def addjob(request):
    if request.method == 'POST':
        job = request.POST.get('job')
        fees = request.POST.get('fees')  # Fixed

        # Get the logged-in labour from session
        labour_id = request.session.get('labour_id')

        if labour_id:
            try:
                labour = Labour.objects.get(id=labour_id)

                # Save the job
                Profession.objects.create(
                    labour=labour,
                    profession=job,
                    fees=fees
                )
                return redirect('addjob')  # Replace with your success page
            except Labour.DoesNotExist:
                return render(request, "labour/addjob.html")
        else:
            return redirect('/authsystem/login_attempt/')  # Or show an error message

    return render(request, "labour/addjob.html")