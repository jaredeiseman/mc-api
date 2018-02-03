from rest_framework import viewsets
from api.serializers import *
from api.permissions import *

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrAdmin,)
