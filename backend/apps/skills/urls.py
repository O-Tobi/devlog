from django.urls import path

from .views import SkillsListCreateView, SkillsDetailView  

urlpatterns = [
    path("skill-create/", SkillsListCreateView.as_view(), name="skills-list-create"),
    path("skills/<int:pk>/", SkillsDetailView.as_view(), name="skills-detail"),
]

