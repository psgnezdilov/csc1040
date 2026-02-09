from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import Book, Author

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year', 'author', 'price', 'synopsis', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Book.objects.filter(title__iexact=title).exists():
            raise ValidationError(f"The books with the title {title} already exists.")

        return title

    def clean_year(self):
        year = self.cleaned_data['year']

        if year > date.today():
            raise ValidationError('The Year published cannot be in the future.')
        if year.year < 1440:
            raise ValidationError('The printing press was not invented until 1440.')

        return year

    def clean(self):
        cleaned_data = super().clean()

        year = cleaned_data.get('year')
        author = cleaned_data.get('author')

        if year and author and hasattr(author, 'dob') and year < author.dob:
            raise ValidationError(f'A book cannot be published before its author was born ({author.dob}).')

        return cleaned_data

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'dob', 'country']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Author.objects.filter(name__iexact=name).exists():
            raise ValidationError(f"The author with the name {name} already exists.")

        return name

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob > date.today():
            raise ValidationError("An author cannot be from future")

        return dob