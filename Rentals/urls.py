from django.urls import path, include
from Rentals import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tenants', views.TenantViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'leases', views.LeaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]