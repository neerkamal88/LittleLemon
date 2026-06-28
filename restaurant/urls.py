from django.urls import path, include
from rest_framework import routers

from .views import MenuItemViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]