from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate
# Create your views here.

def signup (request):
    # if request.user.is_authenticated:
    #     messages.warning(request,"You are logged in")
    #     return redirect('index')

    # else:
    form_details = CustomUserForm
    if request.method =='POST':
        form_details = CustomUserForm(request.POST)
        if form_details.is_valid():
            form_details.save()
            messages.success(request,"Registered succecfully")
            return redirect('login')
        # form_details = CustomUserForm
    context = {'form' : form_details}
    return render(request,"signup.html", context)
