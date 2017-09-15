from rest_framework.pagination import (
    PageNumberPagination
)


class NotePageNumberPagination(PageNumberPagination):
    page_size = 5
