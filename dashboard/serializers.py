# serializers.py

from rest_framework import serializers
from dashboard.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount', 'added_at']
