
from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
	image = models.ImageField(upload_to='users_images', null=True , blank=True)
	friends = models.ManyToManyField('user', related_name = "myfriends" , blank=True)

class ChatMessage(models.Model):
	body = models.TextField()
	msg_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_sender")
	msg_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="msg_receiver")
	seen = models.BooleanField(default=False)
	
	def __str__(self):
		return self.body