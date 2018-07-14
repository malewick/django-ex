from django.db import models

TAGS_CHOICES = [
		    ("conference", "conference"),
		    ("popularization", "popularization"),
		    ("award", "award"),
		    ("collaboration", "collaboration"),
		    ("organization", "organization"),
		    ("job", "job"),
		    ("project", "project"),
		    ("seminar", "seminar"),
		]

class Post(models.Model):

    # Title
    title = models.CharField(max_length=140)
    # Short description - assumed present
    short = models.TextField(null=True,blank=True)
    # Long description - if none preset, then 'short' is used as body
    body = models.TextField(null=True,blank=True)
    # dates are optional
    datefrom = models.DateField(blank=True,null=True)
    dateto   = models.DateField(blank=True,null=True)
    place = models.CharField(max_length=140,null=True,blank=True)
    link1 = models.URLField(blank=True,null=True)
    link2 = models.URLField(blank=True,null=True)
    link3 = models.URLField(blank=True,null=True)
    tag1 = models.CharField(max_length=240, choices=TAGS_CHOICES, blank=True)
    tag2 = models.CharField(max_length=240, choices=TAGS_CHOICES, blank=True)
    tag3 = models.CharField(max_length=240, choices=TAGS_CHOICES, blank=True)
    picture1 = models.ImageField(upload_to='pictures',null=True,blank=True)
    picture2 = models.ImageField(upload_to='pictures',null=True,blank=True)
    picture3 = models.ImageField(upload_to='pictures',null=True,blank=True)
    file1 = models.FileField(upload_to='files',null=True,blank=True)
    file2 = models.FileField(upload_to='files',null=True,blank=True)
    file3 = models.FileField(upload_to='files',null=True,blank=True)

    def __str__(self):
        return self.title
