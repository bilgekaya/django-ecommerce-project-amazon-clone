from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse

# Admin Login View
def adminLogin(request):
    # Eğer kullanıcı zaten giriş yaptıysa, admin home sayfasına yönlendir
    if request.user.is_authenticated:
        return redirect('admin_home')

    # Kullanıcı giriş yapmak için POST isteği gönderdiğinde
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Kullanıcıyı authenticate et
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Kullanıcı doğruysa giriş yap
            login(request, use
