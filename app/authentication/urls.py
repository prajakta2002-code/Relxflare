from django.urls import path
from . import views
urlpatterns = [
     path('',views.authlogin, name='login'),
     path('register/',views.authregistration1, name='authregistration1'),
     path('forget-password/',views.forgetpassword, name='forgetpassword'),
     path('logout/',views.authlogout, name='logout'),
]