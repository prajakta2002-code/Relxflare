from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, 'Email or Password Invalid!')
    return render(request,'authentication/login.html')
def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully !')
    return redirect('login')
def authregistration(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('index')
        else:
            messages.error(request, 'Password and Confirm Password Not Matched')
    return render(request,'authentication/signup.html')
def forgetpassword(request):
    return render(request,'authentication/forget.html')




def authregistration1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exist') 
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('profile')

        else:
            messages.error(request, 'Password and Confirm Password Not Matched')

    return render(request,'authentication/registration.html')