from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api.views import (
    CategoryViewSet, SubCategoryViewSet
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
