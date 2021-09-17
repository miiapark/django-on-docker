from rest_framework.serializers import ModelSerializer
from test.models import Message


class TestSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"
