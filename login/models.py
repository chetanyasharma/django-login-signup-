from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    mobile_number_1 = models.CharField(max_length=50,blank=True)
    mobile_number_2 = models.CharField(max_length=50,blank=True)
    mobile_number_3 = models.CharField(max_length=50,blank=True)
    mobile_number_4 = models.CharField(max_length=50,blank=True)
    mobile_number_5 = models.CharField(max_length=50,blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
