from django.contrib.auth.forms import AuthenticationForm , UserCreationForm ,UserChangeForm
from users.models import User , ChatMessage
from django import forms
from django.forms import ModelForm

class UserLoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))

	class Meta:
		model = User
		fields = ('username' , 'password')

class UserRegistrationForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input' , 'placeholder': 'Уведіть'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input' , 'placeholder': 'Уведіть'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))

	

	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email', 'password1','password2' )

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)
		for field_name , filed in self.fields.items():
			filed.widget.attrs['class'] = 'input'

class UserProfileForm(UserChangeForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input' , 'placeholder': 'Уведіть' , 'readonly': True}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input' , 'placeholder': 'Уведіть' , 'readonly': True}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Уведіть'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={ 'placeholder': 'Уведіть'}),required=False)
	
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Уведіть' , 'readonly': True}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'image', 'email' )



class ChatMessageForm(ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class' : 'inputmsg' , 'rows':3, 'placeholder': 'Уведіть ' }))
	class Meta:
		model = ChatMessage
		fields = ('body', )