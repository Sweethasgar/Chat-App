from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="img",blank=True,null=True)
    friends=models.ManyToManyField('Friend',related_name="my_friends")

    def __str__(self):
        return self.name

class Friend(models.Model):
    profile=models.OneToOneField(Profile,on_delete= models.CASCADE)


    def __str__(self):
        return self.profile.name

class Chattmessage(models.Model):
    body=models.TextField()
    msg_sender=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="message_sender")
    msg_receiver=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="message_receiver")
    seen=models.BooleanField(default=False)

    def __str__(self):
        return self.body

    
