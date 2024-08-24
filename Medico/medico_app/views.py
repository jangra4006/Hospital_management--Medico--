from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    df1 = spl_db.objects.all()
    paginator = Paginator(df1,3)
    page = request.GET.get("page")
    page = paginator.get_page(page)
    
    count=paginator.count
    num_pages = paginator.num_pages
    

    df2 = med_camp
    df3 = df2.objects.all()
    
    return render(request, 'index.html',{'page':page,'num_pages':num_pages, 'count':count,'data':df1, 'data2':df3})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=username, password= pass1)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Signin Successfully.")
            return redirect('/')
        else:
            messages.info(request,'Invalid password or username')
            return redirect('signin')
    return render(request, 'signin.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already used")
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username not available")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=pass1, first_name=firstname, last_name=lastname, email=email)
                user.save()
            return redirect('/')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('signup')
    return render(request, 'signup.html')

def signout(request):
    auth.logout(request)

    return render(request, 'index.html')


def appointment1(request):
    if request.method=='POST':
        name = request.POST['name']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user = appointment3.objects.create(name = name, gender = gender, phone = phone, email = email, message = message)
        user.save()
        return redirect('/')
    return render(request, 'appointment.html')























# Calculator
def calc(request):
    return render(request,'main.html')
    
def add(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    result = n1+n2
    return render (request, 'result.html', {'res':result,'a':'Addition'})


def sub(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    result = n1-n2
    return render (request, 'result.html', {'res':result,'a':'Subtraction'})


def mult(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    result = n1*n2
    return render (request, 'result.html', {'res':result,'a':'Multiplication'})


def div(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    result = n1/n2
    return render (request, 'result.html', {'res':result,'a':'Division'})