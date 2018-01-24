from rest_framework import viewsets
from api.models import TestModel
from api.serializers import TestModelSerializer

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
