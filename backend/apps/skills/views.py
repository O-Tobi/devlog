from django.shortcuts import render
from rest_framework import generics
from .models import Skill
from .serializers import SkillsSerializer
from rest_framework.permissions import  IsAuthenticated





# this view will be used to list all skills for the authenticated user and also create a new skill for the authenticated user
class SkillsListCreateView(generics.ListCreateAPIView):
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# this view will be used to retrieve, update and delete a skill for the authenticated user
class SkillsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)