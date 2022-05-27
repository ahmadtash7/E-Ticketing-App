from django.shortcuts import render, redirect
from events.models import Event, Organizer
from accounts.models import User_Account, User_Event
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
from datetime import datetime, tzinfo, timedelta, timezone,time
# import schedule
# import time
import pytz
# Create your views here.


def checkTicket():
    naive = datetime.now()
    utc = pytz.utc
    gmt5 = pytz.timezone('Etc/GMT+5')
    now = utc.localize(naive).astimezone(gmt5)
    reserved = User_Event.objects.filter(purchase_type='R')
    for ticket in reserved:
        time_elapsed = now - ticket.date_bought
        if time_elapsed > timedelta(minutes=2):
            event_name = ticket.EventName
            event = Event.objects.filter(name=event_name).first()
            print(event)
            event.tickets_sold -= 1
            event.tickets_left += 1
            event.save()
            print(time_elapsed)
            ticket.delete()


def Index(request):
    checkTicket()
    events = Event.objects.all()
    society = Organizer.objects.all()
    return render(request, 'index.html', context={'events': events, 'society': society})


def Events(request, oid):
    checkTicket()
    event_data = Event.objects.filter(name=oid).first()
    ticket_bought = False
    if request.user.is_authenticated:
        current_user = request.user
        user_event_data = User_Event.objects.filter(user_username=current_user.username).first()

        if user_event_data is not None:
            ticket_bought = str(current_user.username) == str(user_event_data.user_username) and str(event_data.name) == str(user_event_data.EventName)

        else:
            ticket_bought = False

        print( ticket_bought)
        return render(request, 'event_page.html', context={'event_data': event_data,
         'ticket_bought':ticket_bought,})



    else:
        return render(request, 'event_page.html', context={'event_data': event_data,
         })

def Tickets(request,oid):
    checkTicket()
    event_data = Event.objects.filter(name=oid).first()
    current_user = request.user
    return render(request, 'ticketdetails.html', context={'current_user': current_user,'event_data':event_data})



# def job():
#     print("I'm working...")
#
# schedule.every(1).minutes.do(job)


def SignUp(request):
    checkTicket()
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
    checkTicket()
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
    checkTicket()
    logout(request)
    return redirect('index')


def Buy(request, oid):
    checkTicket()
    event_data = Event.objects.filter(name=oid).first()
    return render(request, 'buy.html',context={'event_data':event_data})



def Pay(request,oid):
    checkTicket()
    event_data = Event.objects.filter(name=oid).first()

    event_data.tickets_left -= 1
    event_data.tickets_sold +=1
    event_data.save()
    current_user = request.user
    user_event = User_Event(user_username=current_user,EventName=event_data,purchase_type='B',date_bought=datetime.now())
    user_event.save()

    return redirect('index')


def Reserve(request,oid):
    checkTicket()
    event_data = Event.objects.filter(name=oid).first()

    event_data.tickets_left -= 1
    event_data.tickets_sold +=1
    event_data.save()
    current_user = request.user
    user_event = User_Event(user_username=current_user,EventName=event_data,purchase_type='R',date_bought=datetime.now())
    user_event.save()

    return redirect('index')
