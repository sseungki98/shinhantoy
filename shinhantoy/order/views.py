from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .serializers import OrderListSerializer, CommentCreateSerializer, CommentSerializer
from .models import Order, Comment

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        return Order.objects.filter(pk=pk)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

class CommentCreateView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
        