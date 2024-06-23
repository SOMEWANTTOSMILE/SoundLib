from rest_framework import serializers
from premium.models import ServiceProduct, UserSubscription
from datetime import datetime, timedelta


class PremiumInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProduct
        fields = ('id', 'name', "description", "price")


class GetPremiumSerializer(serializers.Serializer):
    service_chosen_id = serializers.IntegerField()
    is_active = serializers.BooleanField()
    subscription_period = serializers.CharField()

    def create(self, validated_data):
        subscribed_on = datetime.now()
        periods = {
                "mn": 30,
                "qt": 92,
                "hy": 182,
                "yr": 365
        }
        subscription_period = validated_data['subscription_period']
        expiring_on = subscribed_on + timedelta(periods[f'{subscription_period}'])
        validated_data['subscribed_on'] = subscribed_on
        validated_data['expiring_on'] = expiring_on
        user = self.context['request'].user
        user.save()
        return UserSubscription.objects.create(**validated_data, user=user)


class UserPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'
