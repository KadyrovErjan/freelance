from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'skills', SkillsViewSet, basename='skills')

urlpatterns = [
    path('', include(router.urls)),
    path('project/', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateAPIView.as_view(), name='project_create'),
    path('project/create/<int:pk>', ProjectEditAPIView.as_view(), name='project_edit'),
    path('offer/', OfferListAPIView.as_view(), name='offer_list'),
    path('offer/<int:pk>/', OfferDetailAPIView.as_view(), name='offer_detail'),
    path('offer/create/', OfferCreateAPIView.as_view(), name='offer_create'),
    path('offer/create/<int:pk>', OfferEditAPIView.as_view(), name='offer_edit'),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]