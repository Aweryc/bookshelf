from website import views
from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.home)

    def test_add_book_url_is_resolved(self):
        url = reverse('add_book')
        self.assertEquals(resolve(url).func, views.add_book)

    def test_register_user_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, views.register_user)

    def test_add_author_url_is_resolved(self):
        url = reverse('add_author')
        self.assertEquals(resolve(url).func, views.add_author)

    def test_book_url_is_resolved(self):
        url = reverse('book', args=['1'])
        self.assertEquals(resolve(url).func, views.book)

    def test_delete_url_is_resolved(self):
        url = reverse('delete_book', args=['1'])
        self.assertEquals(resolve(url).func, views.delete_book)

    def test_update_url_is_resolved(self):
        url = reverse('update_book', args=['1'])
        self.assertEquals(resolve(url).func, views.update_book)

