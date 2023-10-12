from django.test import TestCase, Client
from website import views
from website import models
from django.urls import reverse, resolve
from django.http import HttpResponse


class TestViews(TestCase):
    def test_home(self):
        response = Client().get(reverse('home'))
        self.assertEqual(response.status_code, 200, f'Error in a home page.')
        self.assertTemplateUsed(response, 'home.html', f'Error in a home.html page.')

    def test_register(self):
        response = Client().get(reverse('register'))
        self.assertEqual(response.status_code, 200, f'Error in a register page.')
        self.assertTemplateUsed(response, 'register.html', f'Error in a register.html page.')

    def test_add_book(self):
        response = (Client().get(reverse('add_book')))
        self.assertEqual(response.status_code, 302, f'Error in a add_book page.')

    def test_add_author(self):
        response = Client().get(reverse('add_author'))
        self.assertEqual(response.status_code, 302, f'Error in a add_author page.')

    def test_delete_book(self):
        response = Client().get(reverse('delete_book', args=['1']))
        self.assertEqual(response.status_code, 302, f'Error in a delete_book page.')

