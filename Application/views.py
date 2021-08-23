from django.shortcuts import render, redirect
from Application.forms import RegisterForm
from django.views import View

#from django.contrib.auth import logout


def register(request):
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         form.save()
         print('is valid')
         return redirect('/login')
   else:
      form = RegisterForm()
      print('is not valid')
   return render(request, 'register.html', {'form': form})



