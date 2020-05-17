from django import forms
from django.core.validators import EmailValidator
from .models import Book, Author, Genre, Language


# sample only
class AddAuthorForm(forms.Form):
    first_name = forms.CharField(
        max_length=256,
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=256,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        help_text='Please enter your email',
        label='Email',
        validators=[EmailValidator],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Please enter password'
    )
    dob = forms.DateField(
        initial='20020-90-87',
        widget=forms.SelectDateWidget(attrs={'class': 'form-control'})
    )
    death = forms.DateField(
        error_messages={'required': 'Please enter death'},
        widget=forms.SelectDateWidget(attrs={'class': 'form-control'})
    )


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'death')


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            'title',
            'authors',
            'edition',
            'pages',
            'year',
            'language',
            'genre',
            'publisher',
            'description',
            'front_cover',
        )
        widgets = {
            'title': forms.TextInput,
            'authors': forms.SelectMultiple,
        }


class AddLanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = ('language',)