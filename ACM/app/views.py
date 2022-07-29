from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django import utils
from django.conf import settings
from django.core.mail import send_mail
from datetime import timedelta, timezone
import datetime
from django.utils import timezone
import pytz
from appscheduler.schedulers.background import BackgroundScheduler
import datetime as dt
import urllib.parse
import pandas as pd
import json
from django.template import loader
from django.contrib import messages

# Create your views here.

webteam= OurTeam.objects.filter(Q(typeofmember='Web Team'))

def home(request):
    numbers= Counting.objects.get(id=1)
    globalmember = numbers.globalmember
    localmember = numbers.localmember
    eventsno = numbers.eventsno
    yearsofexp = numbers.yearsofexp

    upcomingevents = Events.objects.filter(eventdnt__gte=utils.timezone.now())
    upcomingevents = sorted(upcomingevents, key=lambda x: x.eventdnt)
    if upcomingevents:
        latestevent = upcomingevents[0]
        eventtime = upcomingevents[0].eventdnt
        timeinstring = eventtime.strftime('%Y-%m-%d %H:%M')
        utc = datetime.datetime.strptime(timeinstring,'%Y-%m-%d %H:%M').replace(tzinfo=pytz.UTC)
        localtz = str(utc.astimezone(timezone.get_current_timezone()))
        eventyear = int(localtz[0:4])
        eventmonth = int(localtz[5:7])
        eventday = int(localtz[8:10])
        eventhr = int(localtz[11:13])
        eventmin = int(localtz[14:16])
        curr_time = str(dt.datetime(eventyear,eventmonth,eventday,eventhr,eventmin,0))
        return render(request, 'app/index.html', {'webteam':webteam,'sendtime':curr_time,'latestevent':latestevent,'global':globalmember,'local':localmember,'eventsno':eventsno,'yearsofexp':yearsofexp})    

    return render(request, 'app/index.html', {'webteam':webteam,'global':globalmember,'local':localmember,'eventsno':eventsno,'yearsofexp':yearsofexp})

def ourteam(request):
    
    coreteam= OurTeam.objects.filter(Q(typeofmember='Core Team'))
    webteam= OurTeam.objects.filter(Q(typeofmember='Web Team'))
    socialteam= OurTeam.objects.filter(Q(typeofmember='Social Team'))
    managementteam= OurTeam.objects.filter(Q(typeofmember='Management Team'))

    context = {'coreteam':coreteam,'webteam':webteam,'socialteam':socialteam,'managementteam':managementteam}

    return render(request, 'app/ourteam.html',context)

def about(request):
    return render(request, 'app/about.html',{'webteam':webteam})


def events(request):

    pastevents = Events.objects.filter(eventdnt__lt=utils.timezone.now())
    upcomingevents = Events.objects.filter(eventdnt__gte=utils.timezone.now())
    pastevents = sorted(pastevents, key=lambda x: x.eventdnt, reverse=True)
    upcomingeventsorted = sorted(upcomingevents, key=lambda x: x.eventdnt)
    upcominglink = []
    
    for i in upcomingevents:
        upcominglink.append(generate_google_calendar_link(i.eventdnt,i.eventdnt + timedelta(minutes=60),i.eventTitle,i.eventDescription))
        
    df = pd.DataFrame(list(upcomingevents.values()))
    df['upcominglink'] = upcominglink
    if len(upcominglink) > 0:
        df1 = df.sort_values(by=['eventdnt'])
        json_records = df1.reset_index().to_json(orient ='records',default_handler=str)
        data = []
        data = json.loads(json_records)
        context = {'pastone':pastevents[:1], 'pastothers':pastevents,'webteam':webteam,'upcomingleft':data,'upcomingright':upcomingeventsorted}
        return render(request, 'app/events.html', context)
    else:
        data = []
        context = {'pastone':pastevents[:1], 'pastothers':pastevents,'webteam':webteam,'upcomingleft':data,'upcomingright':upcomingeventsorted}
        return render(request, 'app/events.html', context)



def _to_google_timestring(datetime_obj):
    return datetime_obj.strftime("%Y%m%dT%H%M%SZ")


def generate_google_calendar_link(start_datetime,end_datetime,eventTitle,eventDesc):
    params = {
        'action': "TEMPLATE",
        'text': "{}".format(eventTitle),
        'details': "{}".format(eventDesc),
        'sendNotifications' : True,
        'dates': "{}/{}".format(
            _to_google_timestring(start_datetime), _to_google_timestring(end_datetime)
        )
    }
    return "https://www.google.com/calendar/render?{}".format(urllib.parse.urlencode(params))

def gallery(request):
    gpic = Gallery.objects.all()
    return render(request, 'app/gallery.html',{'gpic': gpic,'webteam':webteam})

def galleryview(request,pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    galleryview = GalleryImage.objects.filter(post=gallery)
    return render(request, 'app/galleryview.html',{'galleryview':galleryview, 'ename':gallery.egname,'webteam':webteam})


def achievements(request):
    achievements = Achievements.objects.all()
    achievements = sorted(achievements, key=lambda x: x.datent, reverse=True)
    context = {'achievements':achievements,'webteam':webteam}
    return render(request, 'app/achievements.html', context)

def contact(request):
    print("Hello")
    if request.method == "POST":
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        contact= request.POST.get('contact','')
        feedback= request.POST.get('message','')
        Contact(name=name, email=email, contact=contact, feedback=feedback).save()
        messages.success(request,'Your response is Successfully submitted.')
        email_from = settings.EMAIL_HOST_USER
        email_to = [email, ]
        msg = loader.render_to_string(
                'app/contactemail.html',
                {
                    'name': name,
                    'feedback':feedback
                }
            )
        send_mail('Your Response is recorded!!',name ,email_from, email_to, fail_silently=True, html_message=msg)
        return redirect("home")

    return render(request, 'app/about.html',{'webteam':webteam})


def subscribe(request):
    subscribeusers = Subscribe.objects.all()
    subemail = []

    for i in subscribeusers:
        subemail.append(i.email)

    if request.method =="POST":
        email= request.POST.get('email','')
        if email not in subemail:
            Subscribe(email=email).save()
            messages.success(request,'Your subscription has been successfully.')
            return redirect("home")
        else:
            messages.error(request,"You're already Subscribed.")
            return redirect("home")


def Memform(request):
    if request.method == "POST":
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        contact= request.POST.get('contact','')
        sem= request.POST.get('sem','')
        dept= request.POST.get('dept','')
        LocalmemberForm(name=name, email=email, contact=contact, sem=sem, dept=dept).save()
        messages.success(request,'Your form is Successfully submitted.')
        email_from = settings.EMAIL_HOST_USER
        email_to = [email, ]
        msg = loader.render_to_string(
                'app/localformemail.html',
                {
                    'name': name,
                }
            )
        send_mail('LDCE ACM Local Membership',name ,email_from, email_to, fail_silently=True, html_message=msg)
        return redirect("home")

    return render(request, 'app/form.html',{'webteam':webteam})       



#**********************  subscribe mail code **********************


# from email.mime.image import MIMEImage
# from django.core.mail import EmailMultiAlternatives
# from pathlib import Path
# from django.contrib.staticfiles import finders


upcomingevents = Events.objects.filter(eventdnt__gte=utils.timezone.now())
upcomingevents = sorted(upcomingevents, key=lambda x: x.eventdnt)
# eventImage = upcomingevents[0].eventImage.url
# print(eventImage)

# domain = 'http://127.0.0.1:8000'
# img_url = str(domain)+str(eventImage)
# print(img_url)



# subject = 'Django sending email'
# body_html = '''

# '''


# message = EmailMultiAlternatives(
#     subject=subject,
#     body=body_html,
#     from_email=settings.EMAIL_HOST_USER,
#     to=['2001vedant@gmail.com'])

# def logo_data():
#     with open(finders.find('app/images/bg.png'), 'rb') as f:
#         logo_data = f.read()

# def logo_data():    
#     logo = MIMEImage(eventImage)
#     logo.add_header('Content-ID', '<logo>')
#     return logo

# message.mixed_subtype = 'related'
# message.attach_alternative(body_html, "text/html")
# message.attach(logo_data())

# message.send(fail_silently=False)


# #####      Automatic Mail Sender

def send_email():

    subscribeusers = Subscribe.objects.all()
    subemail = []

    upcomingevents = Events.objects.filter(eventdnt__gte=utils.timezone.now())
    upcomingevents = sorted(upcomingevents, key=lambda x: x.eventdnt)
    # eventImage = upcomingevents[0].eventImage

    for i in subscribeusers:
        subemail.append(i.email)

    email_user = subemail
    # server = smtplib.SMTP ('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

    #EMAIL
    message = loader.render_to_string(
                'app/eventmail.html',
                {
                    'upcomingevents':upcomingevents 
                }
            )

    send_mail('Upcoming Event!!', 'ACM',settings.EMAIL_HOST_USER,email_user, fail_silently=True, html_message=message)
    # server.sendmail(settings.EMAIL_HOST_USER, email_user, message)
    print('send email')
    # server.quit()


scheduler = BackgroundScheduler(timezone="Asia/Kolkata")
scheduler.start()

def reminder():
    upcomingevents = Events.objects.filter(eventdnt__gte=utils.timezone.now())
    upcomingevents = sorted(upcomingevents, key=lambda x: x.eventdnt)
    if len(upcomingevents) > 0:
        eventtime = upcomingevents[0].eventdnt
        timeinstring = eventtime.strftime('%Y-%m-%d %H:%M')
        utc = datetime.datetime.strptime(timeinstring,'%Y-%m-%d %H:%M').replace(tzinfo=pytz.UTC)
        localtz = str(utc.astimezone(timezone.get_current_timezone()))
        eventyear = int(localtz[0:4])
        eventmonth = int(localtz[5:7])
        eventday = int(localtz[8:10])
        eventhr = int(localtz[11:13])
        eventmin = int(localtz[14:16])
        send_time = dt.datetime(eventyear,eventmonth,eventday,eventhr,eventmin,0)
        curr_time =dt.datetime.now()
        if send_time.year == curr_time.year:
            if send_time.month == curr_time.month:
                if send_time.day == curr_time.day:
                    if send_time.hour - 2 == curr_time.hour:
                        if send_time.minute - 1 == curr_time.minute:
                            send_email()
            
scheduler.add_job(reminder, 'interval', seconds= 45)
