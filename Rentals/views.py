from django.shortcuts import render
from .models import Tenant, Room, Lease
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound




from .serializers import TenantSerializer, RoomSerializer, LeaseSerializer  

# Create your views here.
class TenantViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    @action(detail=True, methods=['get'])
    def tenantleases(self,request, pk=None):
        permission_classes = [permissions.IsAuthenticated]
        try:
            tenant = self.get_object()
            leases = tenant.leases.all()
            serializer = LeaseSerializer(leases, many=True)
            return Response(serializer.data)
        except Tenant.DoesNotExist:
            raise NotFound("Tenant not found.")

class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    @action(detail=False, methods=['get'])
    def viewvacant(self, request):
        permission_classes = [permissions.IsAuthenticated]
        vacant_rooms = Room.objects.filter(is_occupied=False)
        return Response({'vacant_rooms': vacant_rooms}, status=200)


class LeaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer

    def perform_create(self, serializer):
        room = serializer.validated_data['room']

        if room.is_occupied:
            raise ValidationError("This room is already occupied.")

        lease = serializer.save()
        room.is_occupied = True
        room.save()

    @action(detail=True, methods=['post'])
    def terminate(self, request, pk=None):
        lease = self.get_object()
        if not lease.is_active:
            raise ValidationError("This lease is already terminated.")
        try:
            lease.is_active = False
            lease.save()

            lease.room.is_occupied = False
            lease.room.save()

            return Response(
                {"message": "Lease terminated successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            raise ValidationError(str(e))