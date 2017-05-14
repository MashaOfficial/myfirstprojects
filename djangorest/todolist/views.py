from django.shortcuts import render
from rest_framework.exceptions import NotFound

# Create your views here.

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import permissions
from rest_framework import generics, viewsets
from .serializers import TaskSerializer, TasklistSerializer
from .models import Task, Tasklist, Tags
from django.contrib.auth import get_user_model
from .serializers import TaskSerializer, UserSerializer
from .serializers import TagsSerializer
from django.http import JsonResponse
from .permissions import IsOwner, TaskOwner
from django.core.mail import send_mail

class TasklistCreateView(generics.ListCreateAPIView):
	
	queryset = Tasklist.objects.all()
	serializer_class = TasklistSerializer
	def perform_create(self, serializer):
			"""Save the post data when creating a new bucketlist."""
			serializer.save(owner=self.request.user)

	permission_classes = (
		permissions.IsAuthenticated, IsOwner)



class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Tasklist.objects.all()
	serializer_class = TasklistSerializer
	permission_classes = (
		permissions.IsAuthenticated, IsOwner)


class TaskCreateView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated, TaskOwner)
	serializer_class = TaskSerializer
	
	def get_queryset(self):
		queryset = Task.objects.all()
		list_id = self.kwargs.get('list_id', None)
		if list_id is not None:
			queryset = queryset.filter(tasklist_id = list_id)
		return queryset
 
	def perform_create(self, serializer):
		list_id = self.kwargs.get('list_id', None)
		try:
			tasklist = Tasklist.objects.get(pk=list_id)
		except Tasklist.DoesNotExist:
			raise NotFound()
		serializer.save(tasklist=tasklist)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated, IsOwner)
	serializer_class = TaskSerializer
	


	def get_queryset(self):
		queryset = Task.objects.all()
		list_id = self.kwargs.get('list_id', None)
		if list_id is not None:
			queryset = queryset.filter(tasklist_id = list_id)
		return queryset


class TaskViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated, TaskOwner)
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	

class TagCreateView(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Tags.objects.all()
	serializer_class = TagsSerializer


from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserView(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		user = serializer.instance
		user.set_password(request.data.get('password'))
		user.save()
		
		return JsonResponse({'Congratulations' : 'You have successfully registered!!!'})

'''
class CreateUserView(generics.CreateAPIView): 
	# provide only POST Method
	model = get_user_model()
	permission_classes = (AllowAny,)
	serializer_class = UserSerializer




from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User

from django.core.mail import send_mail





from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Электронный адрес'}))
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class RegisterFormView(FormView):
	form_class = RegistrationForm
	# email = RegistrationForm.email
   
	def form_valid(self, form):
		# Создаём пользователя, если данные в форму были введены корректно.
		form.save()
		emailto = self.kwargs.get('email')

		send_mail('Regist', 'you are reg!!!', 'myapp@mail.ru',
			[emailto], fail_silently=False)


		# Вызываем метод базового класса
		return super(RegisterFormView, self).form_valid(form)

	 # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
	# В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
	success_url = "/login/"

	# Шаблон, который будет использоваться при отображении представления.
	template_name = "register.html"



from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

class LoginFormView(FormView):
	form_class = AuthenticationForm

	# Аналогично регистрации, только используем шаблон аутентификации.
	template_name = "login.html"

	# В случае успеха перенаправим на главную.
	success_url = "/todolists/"

	def form_valid(self, form):
		# Получаем объект пользователя на основе введённых в форму данных.
		self.user = form.get_user()

		# Выполняем аутентификацию пользователя.
		login(self.request, self.user)
		return super(LoginFormView, self).form_valid(form)

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

class LogoutView(View):
	def get(self, request):
		# Выполняем выход для пользователя, запросившего данное представление.
		logout(request)

		# После чего, перенаправляем пользователя на главную страницу.
		return HttpResponseRedirect("/todolists/")


'''
