from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Note

class NoteTests(APITestCase):
    def test_notes_can_be_created(self):
        """
        Ensure we can create a new note object.
        """
        url = reverse('note-list')
        data = {'title': 'Test Note', 'content': 'This is a test note with enough characters.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_error_occurs_if_description_is_less_than_10_chars_long(self):
        """
        Ensure we get an error if the content is less than 10 characters.
        """
        url = reverse('note-list')
        data = {'title': 'Short Note', 'content': 'Short'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('content', response.data)
        self.assertEqual(response.data['content'][0], "Content must be at least 10 characters long.")
