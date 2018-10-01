from rest_framework import serializers
from .models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'name', 'slug', 'description', 'status',
        )
        read_only_fields = (
            'slug', 'created_at', 'updated_at', 'deleted_at'
        )


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            'id', 'category', 'name', 'slug', 'description',
            'status',
        )
        read_only_fields = (
            'slug', 'created_at', 'updated_at', 'deleted_at'
        )
