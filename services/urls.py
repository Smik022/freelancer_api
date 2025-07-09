from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = router.urls
