from rest_framework import serializers
from .models import Skill


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:     
        model = Skill
        fields = ('id', 'user', 'name', 'created_at')
        read_only_fields = ('user',)


class CreateSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('user', 'name')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        
        return Skill.objects.create(
            user=user,
            **validated_data
        )

