from django.urls import path
from .views import LogView, LogListCreateView, LogDetailView    

urlpatterns = [
    path("logs/", LogView.as_view(), name="logs"),
    path("log-create/", LogListCreateView.as_view(), name="logs-list-create"),
    path("logs/<int:pk>/", LogDetailView.as_view(), name="logs-detail"),
]

# test log CRUD
