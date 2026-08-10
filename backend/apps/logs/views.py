from django.shortcuts import render
from rest_framework import generics
from .models import Logs
from .serializers import LogSerializer
from rest_framework.permissions import  IsAuthenticated

class LogView(generics.CreateAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogSerializer
    # any authenticated user should be able to create a log but only the creator should be able to fetch and edit
    permission_classes = [IsAuthenticated]



# this view will be used to list all logs for the authenticated user and also create a new log for the authenticated user
class LogListCreateView(generics.ListCreateAPIView):
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Logs.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# this view will be used to retrieve, update and delete a log for the authenticated user
class LogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logs.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Logs.objects.filter(user=self.request.user)