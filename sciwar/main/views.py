from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from main.models import *
from django.utils import simplejson as json
from datetime import datetime, timedelta
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def main_page(request):
    today_events = Event.objects.filter(start_time__day = datetime.today().day + 0).order_by('start_time')

    current_events = Event.objects.filter(
        start_time__lte = datetime.now()
    ).filter(end_time__gte = datetime.now())

    other_events = Event.objects.all().order_by('start_time')

    current_info = []

    for event in current_events:
        kaist_players = []
        postech_players = []
        recent_comments = []
        if(event and event.is_competition):
            kaist_players = event.kaist_players.all().order_by('year')
            postech_players = event.postech_players.all().order_by('year')
        if event:
            recent_comments = CheerMessage.objects.filter(event = event.id).order_by('-time')[:5]
        current_info.append([event,kaist_players,postech_players,recent_comments])


    current_time = datetime.now()
    response = render(request, 'index.html', {
        "state":_get_state(),\
        "today_events":today_events,\
        "live":current_events,\
        "current_info":current_info,\
        "other_events":other_events,\
        "current_time":current_time,\
    })
    token = request.COOKIES.get('sciwar_live_token','')
    if token == '':
        response.set_cookie('sciwar_live_token',_get_user_key(),expires=datetime.now() + timedelta(3,0))
    else :
        response.set_cookie('sciwar_live_token',token,expires=datetime.now() + timedelta(3,0))

    return response


def info_page(request):
    return render(request, 'info.html', {"state":_get_state()})


def schedule_page(request):
    Month = [0,"JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    current_time = datetime.now()
    date = Month[current_time.month]+" "+str(current_time.day)
    events = _get_schedule()
    num = 0
    for index,event in enumerate(events):
        if event["date"] == date:
            num=index+1

    return render(request, 'schedule.html', {"state":_get_state(), "events":_get_schedule(), "today_date":num})


def map_page(request):
    event = Event.objects.all()
    events = []
    for e in event:
        event_item = {
            'name': e.name,
            'id': e.name.lower().replace(' ', '_').replace('.', ''),
            'building': e.building
        }
        events.append(event_item)
    return render(request, 'map.html', {"state":_get_state(), "events": events})


def video_page(request):
    return render(request, 'video.html', {"state":_get_state()})


def update_information(request):
    avail_notice = True if request.GET.get('notice', False) == "true" else False
    avail_info = True if request.GET.get('information', False) == "true" else False

    contents = []
    informations = Info.objects.all()
    for info in informations:
        item = {
                'title': info.title,
                'article': info.content,
                'classify': info.get_category_display(),
                'date': info.time.strftime("20%y. %m. %d.")
                }
        if info.category == 1 and avail_notice:
            contents.append(item)
        if info.category == 2 and avail_info:
            contents.append(item)
    return HttpResponse(json.dumps({
        'contents': contents}, ensure_ascii=False, indent=4))


def update_video(request):
    classify = request.GET.get('name','all')
    sort_order = int(request.GET.get('order', 0))

    event_set = []
    if classify == "etc":
        event_set.append("HACKING CONTEST")
        event_set.append("OPENING CEREMONY")
        event_set.append("BEER PARTY")
        event_set.append("CLOSING CEREMONY")
    elif classify != "all":
        event_set.append(classify)

    contents = []
    if sort_order == 1:
        videos = Video.objects.all().order_by('time')
    else:
        videos = Video.objects.all().order_by('-time')
    for video in videos:
        if classify=="all" or video.event.name in event_set:
            item = {
                'title': video.name,
                'event': video.event.name,
                'link': video.link,
                'time': video.time.strftime("20%y. %m. %d. %H:%M")
                }
            contents.append(item)
    return HttpResponse(json.dumps({
        'contents': contents}, ensure_ascii=False, indent=4))


def detail_page(request, event_id):
    event = Event.objects.get(id = event_id)
    kaist_players = event.kaist_players.all()
    postech_players = event.postech_players.all()

    if event.start_time <= datetime.now() and event.end_time >= datetime.now():
        is_live = True
    else:
        is_live = False

    page = request.GET.get('page',1)
    comments_list = CheerMessage.objects.filter(event = event_id).order_by('-time')
    paginator = Paginator(comments_list, 10)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    back=request.GET.get('back','')

    return render(request, 'detail.html', {
        "state":_get_state(),\
        "is_live":is_live,\
        "event":event,\
        "kaist_players":kaist_players,\
        "postech_players":postech_players,\
        "comments":comments,\
        "back":back,\
    })


# private function
def _get_state():
    state = {}
    events_list = Event.objects.all()

    state["KAIST"] = 0
    state["POSTECH"] = 0
    state["ALL"] = len(events_list)
    state["DONE"] = 0
    for event in events_list:
        if event.winner == 1:
            state["KAIST"] += event.score
        elif event.winner == 2:
            state["POSTECH"] += event.score
    state["DONE"] = len(Event.objects.filter(end_time__gte = datetime.now()))
    state["live"] = _count_active
    return state


def _get_schedule():
    Month = [0,"JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    events = []
    events_list = sorted(Event.objects.all(), key=lambda k: k.start_time)
    exist_date = []
    for event in events_list:
        if not event.start_time.date() in exist_date:
            exist_date.append(event.start_time.date())
    for date in exist_date:
        events_per_day = []
        for event in events_list:
            if event.start_time.date() == date:
                info = {}
                info["id"] = event.id
                info["name"]= event.name
                info["start_time"] = event.start_time
                info["end_time"] = event.end_time
                info["location"] = event.building
                events_per_day.append(info)
        events.append({"date":Month[date.month]+" "+str(date.day), "events":events_per_day})
    return events


def CheerCreate(request):
    school = request.POST.get('school')
    content = request.POST.get('content')
    event_id = request.POST.get('event')

    try :
        event = Event.objects.get(id=event_id)
    except Exception,e:
        event = None

    if event != None and school in ["1","2","3"] and content.strip() != '':
        cheer = CheerMessage(content=content,event=event,school=school)
        cheer.save()
        return HttpResponseRedirect('/events/%s/#cheer'%event_id)
    else :
        return HttpResponse('<script>alert("Invalid comment");history.go(-1);</script>')


class CheerList(ListView):
    model = CheerMessage
    template_name = 'cheer.html'
    queryset = CheerMessage.objects.order_by('-pk')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CheerList, self).get_context_data(**kwargs)
        context['state'] = _get_state()
        return context


def heartbeat(request):
    token = request.COOKIES.get('sciwar_live_token','')
    response = HttpResponse("OK")
    if token == '':
        response.set_cookie('sciwar_live_token',_get_user_key())
        return response
    else :
        if _set_active(token):
            return response
        else :
            response.set_cookie('sciwar_live_token',_get_user_key())
            return response

def _count_active():
    now = datetime.now()
    live = LiveUser.objects.filter( last_access__gte = now - timedelta(0,1*60))
    unlive = LiveUser.objects.filter( last_access__lt = now - timedelta(0,1*60))
    return len(live)


def _set_active(token):
    try :
        user = LiveUser.objects.get(token=token)
        user.save()
        return True
    except :
        return False


def _get_user_key():
    import string
    import random

    size = 10
    chars = string.ascii_uppercase + string.digits
    new_id = ''.join(random.choice(chars) for x in range(size))
    while len(LiveUser.objects.filter( token = new_id )) != 0:
        new_id = ''.join(random.choice(chars) for x in range(size))
    try :
        user = LiveUser(token=new_id)
        user.save()
        return new_id
    except Exception, e:
        return None


def board(request):
    board_contents = BoardContent.objects.all().order_by('time')

    contents = []
    for content in board_contents:
        item = {
            'id': content.id,
            'title': content.title,
            'time': content.time
        }
        contents.append(content)
    state = _get_state()
    return render(request, 'board.html', {
        "state": _get_state(),
        "contents": contents})


def board_write(request):
    if request.method == "GET":
        return render(request, 'board_write.html', {"state": _get_state()})
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        board_content = BoardContent(title=title, content=content)
        board_content.save()
        return render(request, 'board.html', {"state": _get_state()})
