from django_filters import FilterSet
from .models import  Project


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = {
            'status': ['exact'],
            'category': ['exact'],
            'budget': ['gt', 'lt'],
        }