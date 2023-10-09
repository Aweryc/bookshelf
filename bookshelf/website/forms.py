from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book, Author


# from models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = \
            ('<span class="form-text text-muted"><small>Required. 150 characters or fewer. '
             'Letters, digits and @/./+/-/_ only.</small></span>')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = \
            ('<ul class="form-text text-muted small"><li>Your password can\'t be too similar '
             'to your other personal information.</li><li>Your password must contain at '
             'least 8 characters.</li><li>Your password can\'t be a commonly used password.'
             '</li><li>Your password can\'t be entirely numeric.</li></ul>')

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = \
            ('<span class="form-text text-muted"><small>Enter the same password as '
             'before, for verification.</small></span>')


# Create Add Record Form
class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = ("user", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.none()

        if 'author' in self.data:
            try:
                author_id = int(self.data.get('author'))
                self.fields['author_id'].queryset = Author.objects.filter(country_id=author_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.author_name.city_set.order_by('name')

    title = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Title", "class": "form-control"}), label="")

    author_name = forms.ChoiceField(required=True, widget=forms.widgets.ChoiceWidget(
        attrs={"placeholder": "Author Name", "class": "form-control"}), label="")

    desc = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Description", "class": "form-control"}), label="")

    released_at = forms.DateField(required=True,
                                  widget=forms.widgets.DateInput(
                                      attrs={"placeholder": "Released at", "class": "form-control"}),
                                  label="")

    author_id = forms.IntegerField()

    user_add_id = forms.IntegerField()


