from django.shortcuts import render, redirect, get_object_or_404
from authsystem.models import Labour, Customer
from .models import ChatMessage

def chat_room(request):
    username = request.session.get("username")
    role = request.session.get('role')
    labour = None
    customer = None

    # detect logged-in user type
    if Labour.objects.filter(username=username).exists():
        labour = Labour.objects.get(username=username)
        partners = Customer.objects.all()
    elif Customer.objects.filter(username=username).exists():
        customer = Customer.objects.get(username=username)
        partners = Labour.objects.all()
    else:
        return redirect("/authsystem/login_attempt/")

    selected_partner = None
    messages = []

    # check selected partner (from GET or POST)
    partner_id = request.GET.get("partner_id") or request.POST.get("partner_id_hidden")
    if partner_id:
        if labour:
            selected_partner = get_object_or_404(Customer, id=partner_id)
            messages = ChatMessage.objects.filter(labour=labour, customer=selected_partner)
        elif customer:
            selected_partner = get_object_or_404(Labour, id=partner_id)
            messages = ChatMessage.objects.filter(labour=selected_partner, customer=customer)

    # handle sending message
    if request.method == "POST" and request.POST.get("message"):
        text = request.POST.get("message")
        if labour and selected_partner:
            ChatMessage.objects.create(
                labour=labour,
                customer=selected_partner,
                sender_type="labour",
                message=text
            )
        elif customer and selected_partner:
            ChatMessage.objects.create(
                labour=selected_partner,
                customer=customer,
                sender_type="customer",
                message=text
            )
        return redirect(f"/chat/room/?partner_id={selected_partner.id}")

    return render(request, "chat/chat_room.html", {
        "labour": labour,
        "customer": customer,
        "partners": partners,
        "selected_partner": selected_partner,
        "messages": messages,
        "role":role
    })


def delete_chat(request, labour_id, customer_id):
    labour = get_object_or_404(Labour, id=labour_id)
    customer = get_object_or_404(Customer, id=customer_id)
    ChatMessage.objects.filter(labour=labour, customer=customer).delete()
    return redirect("/chat/room/")
