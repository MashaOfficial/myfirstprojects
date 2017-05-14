from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tasklist(models.Model):
	name = models.CharField(max_length=200)
	# owner = models.ForeignKey(User, related_name="tasklists", on_delete=models.CASCADE, default=1)
	owner = models.ForeignKey('auth.User',  
	related_name='tasklists', 
	on_delete=models.CASCADE) 
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.name)


class Tags(models.Model):
	name = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return "{}".format(self.name)


class Task(models.Model):
	name = models.CharField(max_length=200, blank=True)
	description = models.TextField(max_length=1000, blank=True)
	completed = models.BooleanField(default=False)
	date_created = models.DateField(auto_now_add=True)
	due_date = models.DateField(null=True, blank=True)
	date_modified = models.DateField(auto_now=True)
	tags = models.ManyToManyField(Tags)
	
	owner_of_task = models.ForeignKey('auth.User',  
	related_name='+', 
	on_delete=models.CASCADE, default=2)
	# image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')


	PRIORITY = (
		('h', 'High'),
		('m', 'Medium'),
		('l', 'Low'),
		('n', 'None')
	)

	priority = models.CharField(max_length=1, choices=PRIORITY, default='n')

	tasklist = models.ForeignKey(Tasklist, related_name='tasks', on_delete=models.CASCADE)


	def __str__(self):
		return "{}".format(self.name)


