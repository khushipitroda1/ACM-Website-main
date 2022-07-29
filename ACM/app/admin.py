from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Events)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['eventTitle', 'eventspeakers', 'eventdnt', 'eventDescription', 'eventDate', 'eventDuration', 'eventid', 'eventImage']

@admin.register(OurTeam)
class OurTeamModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','title','typeofmember','gender','desc','linkedlink','instalink','githublink','member_image']


class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage
 
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','egname','egimage']
    inlines = [GalleryImageAdmin]
 
    class Meta:
       model = Gallery
 
@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Achievements)
class AchievementsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'month','year', 'image', 'datent']

@admin.register(Subscribe)
class SubscribeModelAdmin(admin.ModelAdmin):
    list_display = ['email']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','feedback']
    
@admin.register(LocalmemberForm)
class LocalmemberFormModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','sem','dept']

@admin.register(Counting)
class CountingModelAdmin(admin.ModelAdmin):
    list_display = ['id','globalmember','localmember','eventsno','yearsofexp']
    