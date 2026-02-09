from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the Author model."""

    class Meta:
        model = Author
        fields = ['id', 'name', 'dob', 'country']
        read_only_fields = ['id']

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book model."""
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name']
        read_only_fields = ['id']