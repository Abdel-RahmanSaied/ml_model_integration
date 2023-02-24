from django.urls import path
from .views import ModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('model', ModelViewSet, basename='model')

urlpatterns = []

urlpatterns += router.urls