from django.db import models

# Create your models here.

class contact(models.Model):
    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, null=False)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=30, null=True)
    zip = models.CharField(max_length=5, null=True)
    phone = models.CharField(max_length=13, null=True)
    comments = models.TextField(null=True)
    attendees = models.TextField(null=True)
    guestnum = models.IntegerField(null=True)


