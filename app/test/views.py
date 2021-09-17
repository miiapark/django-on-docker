from rest_framework.viewsets import ModelViewSet
from test.models import Message
from test.serializers import TestSerializer


class TestViewSet(ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = TestSerializer

