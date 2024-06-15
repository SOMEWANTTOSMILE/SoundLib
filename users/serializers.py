from rest_framework import serializers
from users.models import CustomUser


class FillingProfileSerializer(serializers.Serializer):
    alias = serializers.CharField()
    phone_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def update(self, instance, validated_data):
        instance.alias = validated_data.get('alias')
        instance.phone_number = validated_data.get('phone_number')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.save()
        return instance
