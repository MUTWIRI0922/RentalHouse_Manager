from django.shortcuts import render
from .models import Tenant, Room, Lease
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view


from .serializers import TenantSerializer, RoomSerializer, LeaseSerializer  

# Create your views here.
class TenantViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class LeaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer