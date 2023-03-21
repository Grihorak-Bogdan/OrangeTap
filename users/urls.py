from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
	path('edit/', views.edit , name='edit'),

	path('logout/', views.logout , name='logout'),
	path('login/', views.login , name='login'),
	path('', views.main_page , name='main_page'),
	path('register/', views.register , name='register'),
	
	path('direct/', views.direct , name='direct'),
	path('friend/<int:id>/', views.chat , name="chat"),
	path('sent_msg/<int:id>/', views.sentMessages, name = "sent_msg"),
	path('rec_msg/<int:id>/', views.receivedMessages, name = "rec_msg"),
	path('notification', views.chatNotification, name = "notification"),
	path('@<str:username>', views.profile , name='profile'),
]
