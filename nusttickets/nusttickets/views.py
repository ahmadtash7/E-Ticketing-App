from django.shortcuts import render
from events.models import Event, Organizer
from django.urls import reverse_lazy
from accounts import forms
from django.views.generic.edit import CreateView
# Create your views here.
def Index(request):
    events = Event.objects.all()
    society = Organizer.objects.all()
    return render(request, 'index.html',context={'events':events,'society':society})

def Events(request, oid):
    event_data = Event.objects.filter(name=oid).first()
    return render(request,'event_page.html', context={'event_data':event_data})

def Tickets(request):

    return render(request, 'ticketdetails.html')

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
