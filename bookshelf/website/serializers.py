from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    desc = serializers.CharField()
    author = serializers.CharField()
    released_at = serializers.IntegerField()
    created_at = serializers.DateTimeField()
