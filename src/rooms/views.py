from django.shortcuts import render
from .models import Events

# Create your views here.
def get_events(request):
    all_events = Events.objects.all()
    events_by_type = Events.objects.only('event_type')
    # if filters applied then get parameter and filter
    # filter base on condition. Else return object
    if request.GET:
        event_arr = []
        if request.GET.get('event_type')=='all':
            all_events = Events.objects.all()
        else :
            all_events = Events.objects.filter(event_type__icontains=requet.GET('event_type'))
        for i in all_events :
            event_sub_arr = {}
            event_sub_arr['event_title'] = i.event_title
            event_sub_arr['event_start'] = i.event_start
            event_sub_arr['event_end'] = i.event_end
            event_sub_arr['resource'] = i.resource
            event_sub_arr['event_color'] = i.event_color
            event_sub_arr['description'] = i.description
            event_arr.append(event_sub_arr)
        return HTTPResponse(json.dump(event_arr))
    
    context = {
        "events": all_events,
        "events_by_type": events_by_type,
    }
    return render(request, 'about.html', context)
    

