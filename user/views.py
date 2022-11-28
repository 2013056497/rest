from rest_framework import viewsets
from user.serializers import RestUserSerializer
from user.models import RestUser


class RestUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RestUser.objects.all().order_by('name')
    serializer_class = RestUserSerializer

