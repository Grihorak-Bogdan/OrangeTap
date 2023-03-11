from django.shortcuts import render, HttpResponseRedirect , redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import logout
from users.models import User , Friend , ChatMessage 
from users.form import UserLoginForm , UserRegistrationForm , UserProfileForm , ChatMessageForm
from django.http import JsonResponse
import json
# Create your views here.

def edit(request):
	if request.method == 'POST':
		form = UserProfileForm(instance = request.user , data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:main_page'))
	else:
		form = UserProfileForm(instance = request.user)
	return render(request, 'users/edit.html' ,{
		"auth": request.user.is_active , 
		"form": form ,
	} )


def add_friend(request):
	print(id)
	return HttpResponseRedirect(reverse('users:main_page'))


def login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username , password=password)
			if user and user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('users:main_page'))
			else:
				print(form.errors)
	else:
		form = UserLoginForm()
	form = UserLoginForm()
	context = {'form' : UserLoginForm()}
	return render(request, 'users/login.html' , context)


def main_page(request ):
	all_user = User.objects.all()
	return render(request, 'users/main_page.html' , {
		"all_user" : all_user ,
		"auth": request.user.is_active ,
	})


def register(request ):
	form = UserRegistrationForm()
	user = User.objects.all()
	if request.method == 'POST':
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:login'))
	else:
		form = UserRegistrationForm()
	context = {'form': form}
	return render(request, 'users/register.html' , context)


def profile(request , username ):
	obj = User.objects.get(username=username)
	is_my = request.user.id == obj.id
	return render(request, 'users/profile.html' , {
	'obj': obj , 
	'is_my': is_my ,
	'username':username ,
	"auth": request.user.is_active ,
	})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('users:login'))

def direct(request):
	user = request.user
	friends = user.friends.all()
	return render(request, 'users/direct.html' , {
		"friends": friends, 
		"auth": request.user.is_active ,
	})




def chat(request , id):
	friend = Friend.objects.get(id=id)
	user = request.user
	profile = User.objects.get(id=friend.profile.id)
	chats = ChatMessage.objects.all()
	rec_chats = ChatMessage.objects.filter(msg_sender=profile , msg_receiver=user , seen=False)
	rec_chats.update(seen=True)
	form = ChatMessageForm()
	if request.method == "POST":
		form = ChatMessageForm(request.POST)
		if form.is_valid():
			chat_message = form.save(commit=False)
			chat_message.msg_sender = user
			chat_message.msg_receiver = profile
			chat_message.save()
			return redirect("users:chat", id=friend.profile.id)
		
	return render(request, 'users/chat.html', {
		"friend" : friend, 
		"form" : form,
		"user" : user,
		"profile" : profile ,
		"chats": chats,
		"num": rec_chats.count(),
		"auth": request.user.is_active ,
	})

def sentMessages(request, id):
	user = request.user
	friend = Friend.objects.get(id=id)
	profile = User.objects.get(id=friend.profile.id)
	data = json.loads(request.body)
	new_chat = data["msg"]
	new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen=False )
	return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, id):
	user = request.user
	friend = Friend.objects.get(id=id)
	profile = User.objects.get(id=friend.profile.id)
	arr = []
	chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
	for chat in chats:
		arr.append(chat.body)
	return JsonResponse(arr, safe=False)


def chatNotification(request):
	user = request.user
	friends = Friend.objects.all()
	arr = []
	for friend in friends:
		chats = ChatMessage.objects.filter(msg_sender__id=friend.profile.id, msg_receiver=user, seen=False)
		arr.append(chats.count())
	return JsonResponse(arr, safe=False)