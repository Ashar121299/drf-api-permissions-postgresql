from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import  status
from django.contrib.auth import get_user_model
from .models import Book, Library

from django.urls import reverse

class BookTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_book= Book.objects.create(
            title="book1",
            description="desc1",
            author="test1",
            owner=testuser1,
        )
        test_book.save()

        test_libray= Library.objects.create(
            name="just",
            address='irbid'
        )
        test_libray.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_books_model(self):
        book = Book.objects.get(id=1)
        actual_owner = str(book.owner)
        actual_title = str(book.title)
        actual_description = str(book.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_title, "book1")
        self.assertEqual(actual_description, "desc1")

    def test_library_model(self):
        library = Library.objects.get(id=1)
        actual_name = str(library.name)
        actual_address=str(library.address)
        self.assertEqual(actual_name, "just")
        self.assertEqual(actual_address, "irbid")
        

    def test_get_books_list(self):
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = response.data
        self.assertEqual(len(books), 1)

    def test_get_library_list1(self):
        url = reverse("library_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        libraries = response.data
        self.assertEqual(len(libraries), 1)
        
    def test_auth_required(self):
        self.client.logout()
        url = reverse("book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required1(self):
        self.client.logout()
        url = reverse("library_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("book_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_only_owner_can_delete1(self):
    #     self.client.logout()
    #     self.client.login(username='testuser2', password="pass")
    #     url = reverse("library_detail", args=[1])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)