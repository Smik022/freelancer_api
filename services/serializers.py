from rest_framework import serializers
from .models import Service, Review

class ReviewSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['client', 'created_at']

class ServiceSerializer(serializers.ModelSerializer):
    freelancer = serializers.StringRelatedField(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['freelancer', 'created_at']
