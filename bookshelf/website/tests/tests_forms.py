from django.test import TestCase
from django.contrib.auth.models import User
from website import forms
from website.models import Author, Book


class TestForms(TestCase):

    def test_add_author_form_validate(self):
        """Test form for correct data."""
        data = {
            'id': 1, 'first_name': 'Ffffsdfsdf', 'last_name': 'sadfgsdfgdf', 'dob': '2023-03-02',
            'bio': 'sregsergsaerge',
            'user_add': User()
        }
        form = forms.AddAuthorForm(data)
        self.assertTrue(form.is_valid())

    def test_add_author_form_no_data(self):
        """Test form for empty data. In an Author model 6 attributes.
        One 'created_at' has default value and 'user_add' excludes in a form.
        As result, we have 4 fields should be filled"""
        data = {}
        form = forms.AddAuthorForm(data)
        self.assertEquals(len(form.errors), 4)
