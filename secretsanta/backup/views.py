from django.contrib.auth.forms import UserCreationForm  
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate

def register_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password1'])
            login(request,new_user)
            messages.success(request, 'Account Created Successfully')
            return redirect(reverse_lazy('main:list'))
    else:
        form = UserCreationForm()
    ctx = {'form':form}
    return render(request,'main/register.html',ctx)

