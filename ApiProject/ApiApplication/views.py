from django.shortcuts import render
from . models import Book
from rest_framework.views import APIView
from rest_framework.response import Response

class BookApiView(APIView):
    def get(self, request, *args, **kwargs):
        allBooks = Book.objects.all().values()
        return Response({'message': 'List of Books','allBooks': allBooks})
    def post(self, request, *args, **kwargs):
        Book.objects.create(id=request.data['id'],
                            title=request.data['title'],
                            author=request.data['author'])
        
        book=Book.objects.filter(id=request.data['id']).values()
        return Response({'message': 'New book added', 'book': book})
