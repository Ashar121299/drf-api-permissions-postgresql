
from rest_framework import serializers

from .models import Book,Library
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields=['id','author','title','description','owner']
        # fields='__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model= Library
        fields='__all__'