from django.shortcuts import render
from .models import Order, OrderItem
from rest_framework import viewsets
from .serializer import OrderSerializer, OrderItemSerializer

# Após o comentario "# Create your views here." e crie as views "Order".

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer  


# Create your views here.
