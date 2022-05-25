from django.shortcuts import render, redirect
from events.models import Event, Organizer
from accounts.models import User_Account
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.


def Index(request):
    events = Event.objects.all()
    society = Organizer.objects.all()
    return render(request, 'index.html', context={'events': events, 'society': society})


def Events(request, oid):
    event_data = Event.objects.filter(name=oid).first()
    return render(request, 'event_page.html', context={'event_data': event_data})


def Tickets(request):
    current_user = request.user
    return render(request, 'ticketdetails.html', context={'current_user': current_user})


def SignUp(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('Email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'bhattiboy01@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(
                request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form, 'title': 'reqister here'})


def LoginView(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account does not exist please sign up')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def LogoutView(request):
    logout(request)
    return redirect('index')


def Buy(request):
    return render(request, 'buy.html')


def Pay(request):
    return render(request, 'index.html')