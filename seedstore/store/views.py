from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')


# def signup(request):
    
#     if request.method == "POST":
#         firstname = request.POST ['firstname']
#         lastname = request.POST ['lastname']
#         username = request.POST ['username']
#         email = request.POST ['email']
#         password = request.POST ['password']
#         confirm_password = request.POST ['confirm_password']
#         phone_number = request.POST ['phone_number']
        
#         # myuser = User.object.create_user(firstname,lastname,username,email,password,confirm_password,phone_number) 
#         # myuser.save()
#          # Corrected: Use User.objects.create_user to create a new user
#         myuser = User.objects.create_user(username=username, email=email, password=password)
        
#         # You can set other user attributes here if needed (e.g., first_name, last_name)
#         myuser.first_name = firstname
#         myuser.last_name = lastname
#         myuser.save()
#         return redirect('login')
#     return render(request, 'signup.html')

def loginn(request):
    return render(request, 'login.html')