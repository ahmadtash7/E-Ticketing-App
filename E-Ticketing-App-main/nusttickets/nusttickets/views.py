from django.shortcuts import render
from events.models import Event, Organizer
# Create your views here.
def Index(request):
    events = Event.objects.all()
    society = Organizer.objects.all()
    return render(request, 'index.html',context={'events':events,'society':society})

def Events(request, oid):

    event_data = Event.objects.filter(name=oid).first()

    return render(request,'event_page.html', context={'event_data':event_data})
