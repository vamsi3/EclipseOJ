from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

def path(instance, filename):
    return '{}/{}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=path)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    country = CountryField(default='IN')
    institute = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=70, null=True)
    rating = models.IntegerField(default=1500)

    def __str__(self):
        return self.user.username

# @receiver(post_save, sender=User)
# def create_user(sender, instance, created, **kwargs):
#     if not created:
#         return
#     # profile = Profile(user=instance)
#     # profile.save()
#     os.mkdir(os.path.join(os.path.join(os.getcwd(), 'uploads/users/'), str(instance.get_username())))
