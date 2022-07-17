from django.contrib import admin
from django.urls import path
from .views import ProductViewSets, UserApiView

urlpatterns = [
    path('products', ProductViewSets.as_view({'get': 'list', 'post': 'create'})),
    path('products/<str:pk>', ProductViewSets.as_view({'get': 'retrieve', 'post': 'update', 'delete': 'destroy'})),
    path('user', UserApiView.as_view())
]
