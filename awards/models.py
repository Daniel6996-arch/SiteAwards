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

    def save_site(self):
        self.save() 

    def delete_site(self):
        self.delete()

    def _str_(self):
        return self.user.username    

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key = True, verbose_name = 'user', related_name = 'profile', on_delete = models.CASCADE)
    full_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image')
    followers = models.ManyToManyField(User, blank = True, related_name = 'followers')

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()    

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


class Comment(models.Model): 
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    website = models.ForeignKey(Website, on_delete = models.CASCADE)        
