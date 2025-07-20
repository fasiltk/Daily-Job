from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("register_customer/",register_customer,name='register_customer'),
    path("register_labour/",register_labour,name='register_labour'),
    path("login_attempt/",login_attempt,name='login_attempt'),
    path('verify/<auth_token>',verify,name='verify'),
    path("", index, name="index"),
    path("logout_view/",logout_view,name='logout_view'),
    path("change_password/",change_password,name='change_password'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

