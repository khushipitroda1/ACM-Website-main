from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home,name='home'),
    path('ourteam/',views.ourteam,name='ourteam'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events'),
    path('gallery/',views.gallery,name='gallary'),
    path('gallery-view/<int:pk>', views.galleryview, name='gallery-view'),
    path('achievements/', views.achievements, name='achievements'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
    path('form/',views.Memform,name='form'),


] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
