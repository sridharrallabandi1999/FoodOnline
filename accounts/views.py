from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
from django.contrib import messages


def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = user.CUSTOMER
            # user.save()
            # form.save()

            #create ser using create_user_method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,last_name=last_name)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,'Your account has registered sucessully!')
            return redirect ('registerUser')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html',context)
    