from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import BookSerializer,LibrarySerializer
# Create your views here.
from .models import Book,Library
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly

class bookListView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly, IsAuthenticated]

class bookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[IsOwnerOrReadOnly, IsAuthenticated]



class libraryListView(ListCreateAPIView):
    queryset=Library.objects.all()
    serializer_class= LibrarySerializer
    Permission_classes=[IsAuthenticatedOrReadOnly]
    


class libraryDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Library.objects.all()
    serializer_class= LibrarySerializer
    Permission_classes=[IsAuthenticatedOrReadOnly]