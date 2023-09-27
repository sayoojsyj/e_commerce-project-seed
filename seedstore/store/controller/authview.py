from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup (request):
    if request.user.is_authenticated:
        messages.warning(request,"You are logged in")
        return redirect('/')
    else:
        form_details = CustomUserForm()
        if request.method =='POST':
            form_details = CustomUserForm(request.POST)
            if form_details.is_valid():
                form_details.save()
                messages.success(request,"Registered succecfully")
                return redirect('login')
        context = {'form' : form_details}
        return render(request,"signup.html", context)





def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pswrd = request.POST.get('password')
            
            user = authenticate(request, username=name, password=pswrd )
            
            if user is not None:
                login(request, user)
                messages.success(request, "logged in succesfully")
                return redirect("/")
            else:
                messages.success(request, "invalid credentials")
                return redirect('login')
    return render(request, 'login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "loged out succesfully")
        return redirect("/")


