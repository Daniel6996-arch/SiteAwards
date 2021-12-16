from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Website(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 120)
    description = models.TextField()
    country = models.CharField(max_length = 120)
    landing_page = CloudinaryField('Landing page image')
    uploaded_on = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key = True, verbose_name = 'user', related_name = 'profile', on_delete = models.CASCADE)
    full_name = models.CharField(max_length=30)
    bio = HTMLField(blank=True, null=True)
    profile_pic = CloudinaryField('image')
    followers = models.ManyToManyField(User, blank = True, related_name = 'followers')

    @classmethod
    def search_user(cls,search_term):
        users = cls.objects.filter(user__username = search_term)
        return users

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User) 
def save_user_Profile(sender, instance, **kwargs):
    instance.profile.save()     