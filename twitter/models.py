from django.db import models

# Create your models here.

class TwitterSchedulerModel(models.Model):
    tweet = models.TextField(max_length=240)
    tweet_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    sent = models.BooleanField(default=False)
    otp=models.CharField(max_length=50, default='')
    resource_owner_key=models.CharField(max_length=50,default='')
    resource_owner_secret=models.CharField(max_length=50,default='')