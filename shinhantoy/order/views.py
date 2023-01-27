from django.shortcuts import render
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OrderListSerializer, CommentCreateSerializer, CommentSerializer, CommentDeleteSerializer
from .models import Order, Comment

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        order_number = self.request.query_params.get('order_number')
        if order_number:
            orders = Order.objects.filter(ord_no__contains=order_number)
            return orders

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

class CommentView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer
    
    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        return Comment.objects.filter(order_id=order_id)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs) #댓글작성

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs) #댓글보기
        
class CommentDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    serializer_class = CommentDeleteSerializer

    def get_queryset(self):
        mem_id = self.request.user.id
        return Comment.objects.filter(member_id=mem_id)

    def delete(self, request, *args, **kwargs): # 댓글삭제
        return self.destroy(request, args, kwargs)

