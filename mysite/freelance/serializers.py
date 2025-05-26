from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class ProjectSimpleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Project
        fields = ['title', 'category', 'status', 'budget']

class ProjectListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    client = UserProfileListSerializer()
    class Meta:
        model = Project
        fields = ['title', 'category', 'status', 'budget', 'client']

class ProjectDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    client = UserProfileListSerializer()
    class Meta:
        model = Project
        fields = ['title', 'category', 'description', 'deadline', 'status', 'budget', 'skills_required', 'client', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class OfferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class OfferListSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer()
    class Meta:
        model = Offer
        fields = ['project',  'proposed_budget', 'proposed_deadline', 'created_at']

class OfferDetailSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer()
    freelancer = UserProfileListSerializer()
    class Meta:
        model = Offer
        fields = ['project', 'freelancer', 'proposed_budget', 'message', 'proposed_deadline', 'created_at']