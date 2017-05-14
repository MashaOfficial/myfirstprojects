from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Tasklist
from .models import Tags
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	
	password = serializers.CharField(write_only=True)
	
	def created(self, validated_data):
		user = get_user_model().objects.create(
			username = validated_data['username'])
		# assume there is custom auth model or build-in auth model
		# custom auth model can we set by AUTH_USER-MODEL in settings.py
		user.set_password(validated_data['password']) # don't want to serialize password field bcoz it is hashed
		user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ('username', 'password')


class TagsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tags
		fields = ('id', 'name')



class TaskSerializer(serializers.ModelSerializer):
	
	# image = serializers.ImageField(max_length=None, use_url=True)
	tags = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Tags.objects.all())

	class Meta:
		model = Task
		fields = ('id', 'name', 'description', 'completed', 'date_created', 'date_modified', 'due_date', 'tags', 'priority')
		read_only_fields = ('date_created', 'date_modified')


class TasklistSerializer(serializers.ModelSerializer):
	
	tasks = serializers.StringRelatedField(many=True)

	owner = serializers.ReadOnlyField(source='owner.username') # ADD THIS LINE

	class Meta:
		"""Map this serializer to a model and their fields."""
		model = Tasklist
		fields = ('id', 'name', 'tasks', 'owner', 'date_created', 'date_modified') # ADD 'owner'
		read_only_fields = ('date_created', 'date_modified')

'''
	class Meta:
		model = Tasklist
		fields = ('id', 'name', 'tasks')

'''


