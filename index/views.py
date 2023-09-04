# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import tables,subscribe,getID
from .models import shoping_cart1,contact_form
from .models import productlist
# from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def Layout(request):
    
    return render(request,'layout.html')

def Index(request):
    tables_newdata=tables.objects.all()
    # tables_newdata=tables.objects.get(id=7)
    productlistdata=productlist.objects.all().order_by('-id')
    context={
        'tables':tables_newdata,
        'productlist':productlistdata
    }
    if request.method == 'POST':
        id=request.POST.get('id')
        email=request.POST.get('email')
        get_ID=getID(id=id)
        get_ID.save()
        sub_data=subscribe(email=email)
        sub_data.save()
    return render(request,'index.html',context)


def about(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        sub_data=subscribe(email=email)
        sub_data.save()
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        email1=request.POST.get('email1')
        help=request.POST.get('help')
        sub_data1=contact_form(email1=email1,help=help)
        sub_data1.save()
    return render(request,'contact.html')
# def blog(request):
#     if request.method == 'POST':
#         email=request.POST.get('email')
#         sub_data=subscribe(email=email)
#         sub_data.save()
#     return render(request,'blog.html')
def features(request):
    productlistdata=productlist.objects.all()
    context={
      'productlist':productlistdata
    }
    if request.method == 'POST':
        email=request.POST.get('email')
        sub_data=subscribe(email=email)
        sub_data.save()
    return render(request,'features.html',context)

def shop(request):
    productlistdata=productlist.objects.all()
    context={
      'productlist':productlistdata
    }
    if request.method == 'POST':
        email=request.POST.get('email')
        sub_data=subscribe(email=email)
        sub_data.save()
    return render(request,'shop.html',context)

def quickview(request,book_id):

    productlistdata=productlist.objects.get(id=book_id)
    context={
        'productlist':productlistdata
    }
    return render(request,'quickview.html',context)

def home(request):
    productlistdata=productlist.objects.all()
    context={
      'productlist':productlistdata
    }
    return render(request, 'home.html', context)

def quickview(request,id):
    productlistdata=productlist.objects.get(id=id)
    context={
      'productlist':productlistdata
    }
    return render(request, 'quickview.html', context)



def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        messages.success(request, 'Your account has been created successfully.')
        return redirect('index')  # Redirect to your desired page after successful signup
    
    return render(request, 'signup.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')
def shoping_cart(request):
    if request.method == 'POST':
        atm=request.POST.get('atm')
        cvv=request.POST.get('cvv')
        amount=request.POST.get('amount')
        help=request.POST.get('help')
        sub_data2=shoping_cart1(atm=atm,cvv=cvv,amount=amount,help=help)
        sub_data2.save()
    return render(request, 'shoping_cart.html')


# from django.shortcuts import render
# from .models import Book

# def home(request):
#     books = Book.objects.all()
#     return render(request, 'home.html', {'books': books})
