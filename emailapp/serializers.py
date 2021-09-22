from rest_framework import serializers
from .models import EmailDetail

class EmailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDetail
        fields = ('sender')
