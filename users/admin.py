from django.contrib import admin

from users.models import ChatMessage, User

# Register your models here.
admin.site.register([ User,  ChatMessage ])
