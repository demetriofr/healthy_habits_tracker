import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from .models import Habit


# Load test data
with open('core/test_data.json') as f:
    test_data = json.load(f)
    data_test_user_1 = test_data['data_test_user_1']
    data_test_habit_create_1 = test_data['data_test_habit_create_1']
    data_test_habit_create_1_control = test_data['data_test_habit_create_1_control']


class HabitTestCase(APITestCase):
    """Tests for CRUD operations in the habits app."""

    def setUp(self) -> None:

        # Create user and authenticate for tests
        self.user = User.objects.create(email=data_test_user_1['email'])
        self.user.set_password(data_test_user_1['password'])
        self.user.save()
        self.client.force_authenticate(user=self.user)

        # Create habit for test
        self.habit = Habit.objects.create(
            user=self.user,
            **data_test_habit_create_1)

        # Add user to set
        data_test_habit_create_1_control['user'] = self.user.id

    def test_create_habit(self):
        """Test create habit."""
        url_create = reverse('core:habit-create')
        response = self.client.post(url_create, data=data_test_habit_create_1)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check existence object
        self.assertTrue(Habit.objects.filter(action=data_test_habit_create_1['action']).exists())
        # Check the presence of data in one of the required fields
        self.assertEqual(response.json()['place'], data_test_habit_create_1_control['place'])

    def test_habits_owner_list(self):
        """The test checks the output of a list of habits belonging to the user."""
        url_habits_owner_list = reverse('core:my_habits-list')
        response = self.client.get(url_habits_owner_list)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data
        self.assertEqual(response.data['results'][0]['action'], self.habit.action)

    def test_habits(self):
        """The test checks the output of a list of public habits."""
        url_habits_owner_list = reverse('core:habits-list')
        response = self.client.get(url_habits_owner_list)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data
        self.assertIsNone(response.data['next'])

    def test_update_habit(self):
        """The test checks the update of a habit."""
        url_update = reverse('core:habit-update', kwargs={'pk': self.habit.id})
        response = self.client.patch(url_update, data={'action': 'Test action 2'})

        # Check status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data
        self.assertEqual(response.data['place'], data_test_habit_create_1_control['place'])

    def test_delete_habit(self):
        """The test checks the deletion of a habit."""
        url_delete = reverse('core:habit-delete', kwargs={'pk': self.habit.id})
        response = self.client.delete(url_delete)

        # Check status
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
