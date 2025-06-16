from django.urls import path
from .views import OrderByEmailListView, OrderListCreate, OrderRetrieveUpdateDestroy

app_name = 'orders'
urlpatterns = [
    path('orders/', OrderListCreate.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroy.as_view(), name='order-detail'),
    path('admin/orders-by-email/', OrderByEmailListView.as_view(), name='admin-orders-by-email'),
]