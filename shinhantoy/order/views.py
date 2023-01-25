from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import OrderListSerializer
from .models import Order

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)