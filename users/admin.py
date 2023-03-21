from django.contrib import admin
from users.models import User,  ChatMessage
# Register your models here.
admin.site.register([ User,  ChatMessage ])
