from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  

# Create your models here.
class Website(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 120)
    description = models.TextField()
    country = models.CharField(max_length = 120)
    landing_page = CloudinaryField('image')
    uploaded_on = models.DateTimeField(auto_now_add=True)
