from rest_framework import serializers
from .models import Logs


class LogSerializer(serializers.ModelSerializer):
    class Meta:     
        model = Logs
        fields = ('user', 'title', 'content', 'mood', 'log_date', 'skills')
        read_only_fields = ('user',)
        # extra_kwargs = {
        #     'skills': {'required': False}
        # }


class CreateLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        fields = ('user', 'title', 'content', 'mood', 'log_date', 'skills')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        
        return Logs.objects.create(
            user=user,
            **validated_data
        )
