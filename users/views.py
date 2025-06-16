from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsSelf
import logging

logger = logging.getLogger(__name__)

class RegisterCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    
    def perform_create(self, serializer):
        try:
            user = serializer.save()
            logger.info(f"New user registered: {user.email}")
        except Exception as e:
            logger.error(f"Registration failed for {self.request.data.get('email')}: {str(e)}")
            raise

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSelf]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance != request.user:
            logger.warning(f"Unauthorized delete attempt on user {instance.email} by {request.user.email}")
            return Response({"detail": "You can only delete your own account."}, status=403)
        self.perform_destroy(instance)
        return Response(status=204)