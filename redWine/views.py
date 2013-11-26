from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime

def home(request):
    return HttpResponse("<h1>Velkommen til redWine - Vinstraff systemet til dotkom</h1>")

def hello(request):
    return HttpResponse("Hello world")

def dateTime(request):
    now=datetime.datetime.now()
    html="<html><body>The Time Is: %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset=int(offset)
    except:
        raise Http404()
    dt=datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('date.html')
    html = t.render(Context({'current_date': dt}))
    return HttpResponse(html)