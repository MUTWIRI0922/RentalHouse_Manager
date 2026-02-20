from django.shortcuts import render
from .models import Tenant, Room, Lease
from rest_framework import viewsets
from .serializers import TenantSerializer, RoomSerializer, LeaseSerializer  

# Create your views here.
class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer