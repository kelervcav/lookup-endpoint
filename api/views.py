from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Category, SubCategory
)
from .serializers import (
    CategorySerializer, SubCategorySerializer
)
from .utils import CustomPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('status',)
    ordering_fields = ('id',)
    lookup_field = 'id'

    @action(methods=["GET"], detail=True, url_path="sub-categories")
    def subcategory(self, request, id=None):
        category = self.get_object()
        subcat = SubCategory.objects.filter(category=category)
        serializer = SubCategorySerializer(subcat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = CustomPagination
