from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import generics, mixins, status
from .serializers import MemberRegistSerializer, ChangePasswordSerializer
from django.contrib.auth.hashers import check_password, make_password
from .models import Member
from rest_framework.permissions import IsAuthenticated


class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = MemberRegistSerializer


    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        #로그인한 사용자만 들어올 수 있는 곳
        password = request.data.get('password')
        new_password = request.data.get('new_password')
        check_new_password = request.data.get('check_new_password')

        if new_password != check_new_password:
            return Response({
                'detail': 'Wrong New Password',
            },status=status.HTTP_400_BAD_REQUEST)

        member = request.user
        
        if not check_password(password, member.password):
            return Response({
                'detail': 'Wrong Password',
            },status=status.HTTP_404_NOT_FOUND)

        member.password = make_password(new_password)
        member.save()

        return Response(status=status.HTTP_200_OK)


