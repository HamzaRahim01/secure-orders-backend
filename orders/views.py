from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwner
import logging

logger = logging.getLogger(__name__)

class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user)
        if not queryset.exists() and self.request.method == 'GET':
            logger.warning(f"No orders found for user {user.email}")
        return queryset
    
    def perform_create(self, serializer):
        serializer.save()
        

class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
