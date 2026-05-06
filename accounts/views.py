from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from accounts.forms import *


def register(request):
    if request.method == "POST":
        form = AccountCreateForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("account_detail")
    else:
        form = AccountCreateForm() 
    return render(request, "accounts/register.html", {"form": form})


@login_required
def account_detail(request):
    return render(request, "accounts/account_detail.html", {"user": request.user})


@login_required
def account_change(request):
    if request.method == "POST":
        form = AccountChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("account_detail")
    else:
        form = AccountChangeForm(instance=request.user)
        
    return render(request, "accounts/account_change.html", {"form": form})
