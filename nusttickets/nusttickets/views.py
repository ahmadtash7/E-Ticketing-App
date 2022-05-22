from django.shortcuts import render
from events.models import Event, Organizer
# Create your views here.
def Index(request):
    events = Event.objects.all()
    society = Organizer.objects.all()
    return render(request, 'index.html',context={'events':events,'society':society})

def Events(request):

    # event_data = Event.objects.filter(id=oid).first()

    return render(request,'event_page.html')
