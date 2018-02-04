from mc import settings
from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'current_page': self.page.number,
            'page_size': settings.REST_FRAMEWORK['PAGE_SIZE'],
            'count': self.page.paginator.count,
            'results': data
        })