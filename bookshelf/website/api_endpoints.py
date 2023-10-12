from urllib.request import Request

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def books_list_api(request: Request) -> Response:
    """
    :param request: request from client
    :return: json data of all books
    """
    record = Book.objects.all()
    ser_books = BookSerializer(record, many=True)
    return Response(ser_books.data)


@api_view(['GET'])
def book_api(request: Request, pk) -> Response:
    """
    :param request: request from client
    :return: json data of one book with id equals pk
    """
    try:
        record = Book.objects.get(pk=pk)
        one_book = BookSerializer(record)
        return Response(one_book.data)
    except Exception:
        return Response({'message': f'Book # {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)
