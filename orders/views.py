from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Order
from users.models import User
from .serializers import OrderSerializer
from .permissions import IsOwner, IsSuperAdmin
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
        serializer.save(user=self.request.user)

        
class OrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

class OrderByEmailListView(APIView):
  
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        emails = request.data.get('emails', [])
        if not isinstance(emails, list) or not emails:
            logger.warning("Invalid or empty email list provided.")
            return Response({"detail": "A list of emails is required."}, status=status.HTTP400_BAD_REQUEST)

        try:
            users = User.objects.filter(email__in=emails)
            orders = Order.objects.filter(user__in=users).select_related('user')
            serializer = OrderSerializer(orders, many=True)
            logger.info(f"Super admin retrieved {len(orders)} orders for emails: {emails}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Failed to retrieve orders by email: {str(e)}")
            return Response({"detail": "An error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
