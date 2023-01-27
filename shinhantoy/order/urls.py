from django.urls import path
from . import views

urlpatterns = [
    path("", views.OrderListView.as_view()),
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("/<int:order_id>/comment", views.CommentView.as_view()),
    path("/comment/<int:pk>",views.CommentDeleteView.as_view()),
]
