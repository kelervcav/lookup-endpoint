from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10  # Set number of result to display per page
    max_page_size = 50  # Sets max page size that user may request
    page_query_param = 'page'
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'page_number': self.page.number,
            'size_per_page': self.page.paginator.per_page,
            'total_pages': self.page.paginator.num_pages,
            'total': self.page.paginator.count,
            'results': data
        })
