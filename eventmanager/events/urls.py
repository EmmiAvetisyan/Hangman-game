from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet, UserViewSet, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]