from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, home, all_users, FreelancerViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'freelancers', FreelancerViewSet, basename='freelancers')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', home, name='home'),
    path('all/', all_users, name='all_users'),

    # Include router URLs for freelancers
    path('', include(router.urls)),
]
