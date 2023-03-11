from django.contrib import admin
from users.models import User, Friend, ChatMessage
# Register your models here.
admin.site.register([ User, Friend, ChatMessage ])
