import uuid
from django.db import models
from django import utils
# Create your models here.


TITLE_CHOICES = (
('Chair Person','Chair Person'),
('Leader','Leader'),
('Member','Member'),
)

TEAM_CHOICES = (
('Core Team','Core Team'),
('Web Team','Web Team'),
('Social Team','Social Team'),
('Management Team','Management Team'),
)

GENDER_CHOICES = (
('Male','Male'),
('Female','Female'),
)


class Events(models.Model):
    eventTitle = models.TextField(default="Nothing")
    eventspeakers = models.TextField(default="N/A")
    eventDescription = models.TextField(default="Nothing")
    eventImage = models.ImageField(upload_to='eventImg', default="app/images/blog-post-2.jpg")
    eventdnt = models.DateTimeField(default=utils.timezone.now())
    eventDate = models.TextField(default="1-1-1970 - 1")
    eventDuration = models.TextField(default="1pm - 2pm")
    eventid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def str(self):
        return str(self.id)

class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, choices=TITLE_CHOICES)
    role = models.CharField(max_length=200,default="N/A")
    typeofmember = models.CharField(max_length=200, choices=TEAM_CHOICES)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default="Male")
    desc = models.CharField(max_length=500)
    linkedlink = models.CharField(max_length=200)
    instalink = models.CharField(max_length=200)
    githublink = models.CharField(max_length=200)
    member_image = models.ImageField(upload_to='teamMemberImg',default="app/images/team-1-1.jpg")


    def str(self):
        return str(self.id)

class Gallery(models.Model):
    egname = models.CharField(max_length=1000)
    egimage = models.FileField(default="blank",upload_to = 'galleryImage')
    def str(self):
        return str(self.id)

class GalleryImage(models.Model):
    post = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'galleryImage')
 
    def __str__(self):
        return self.post.egname

class Achievements(models.Model):
    title = models.TextField(default="Nothing")
    description = models.TextField(default="Nothing")
    month = models.CharField(max_length=50,default="Nothing")
    year = models.PositiveIntegerField(default=2000)
    image = models.ImageField(upload_to='achievmentsImg')
    datent = models.DateTimeField(default=utils.timezone.now())

    def str(self):
        return str(self.id)

class Subscribe(models.Model):
    email = models.EmailField(max_length=254,unique=True)

    def str(self):
        return str(self.id)


class Contact(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    contact = models.PositiveIntegerField()
    feedback = models.TextField()

    def str(self):
        return str(self.id)
    
class LocalmemberForm(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    contact = models.PositiveIntegerField()
    sem = models.PositiveIntegerField()
    dept = models.CharField(max_length=200)

    def str(self):
        return str(self.id)
    
class Counting(models.Model):
    globalmember = models.PositiveIntegerField(default=0)
    localmember = models.PositiveIntegerField(default=0)
    eventsno = models.PositiveIntegerField(default=0)
    yearsofexp = models.PositiveIntegerField(default=0)

    def str(self):
        return str(self.id)