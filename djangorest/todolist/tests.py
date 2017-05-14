from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Task, Tasklist

class ModelTestCase(TestCase):
    def setUp(self):
        self.task_name = "Выполнить лабораторную работу №9"
        self.task = Task(name=self.task_name)

    def test_model_can_create_task(self):
        old_count = Task.objects.count()
        self.task.save()
        new_count = Task.objects.count()
        self.assertNotEqual(old_count, new_count)




from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .views import TaskCreateView
from .views import TaskDetailsView

'''
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'name': 'Выполнить 9 лабораторную работу',
            'description': 'Прочитать руководство по django rest framework',
            'priority': 'h'
        }
        self.response = self.client.post(reverse('create'), self.task_data, format='json')

    def test_api_can_create_a_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

'''

from django.contrib.auth.models import User

class UserTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd") 
        self.name = "Write world class code"
        # specify owner of a bucketlist
        self.tasklist = Tasklist(name=self.name, owner=user) 


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Since user model instance is not serializable, use its Id/PK
        self.tasklist_data = {'name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('lists'),
            self.tasklist_data,
            format="json")

    def test_api_can_create_a_tasklist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/todolists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_tasklist(self):
        """Test the api can get a given bucketlist."""
        tasklist = Tasklist.objects.get(id=1)
        response = self.client.get(
            '/todolists/',
            kwargs={'pk': tasklist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, tasklist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        tasklist = Tasklist.objects.get()
        change_tasklist = {'name': 'Something new'}
        res = self.client.put(
            reverse('list-detail', kwargs={'pk': tasklist.id}),
            change_tasklist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_tasklist(self):
        """Test the api can delete a bucketlist."""
        tasklist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('list-detail', kwargs={'pk': tasklist.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)