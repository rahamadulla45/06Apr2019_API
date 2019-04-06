from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import (UserCreateAPIView,UserUpdateView,UserDetailView,ItemListView,
    ItemDetailView,CheckOutView,OrderControlAPIView,
    CartDeleteView,CartListView,CartDetailView,OrderDetailView)

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('userupdate/<int:user_id>', UserUpdateView.as_view(), name='userupdate'),
    path('profile/<int:user_id>', UserDetailView.as_view(), name='userupdate'),
    path('list/', ItemListView.as_view(), name='api-list'),
    path('details/<int:item_id>', ItemDetailView.as_view(), name='api-detail'),
    path('checkout/<int:order_id>', CheckOutView.as_view(), name='api-checkout'),
    path('cart/<int:user_id>', CartListView.as_view(), name='api-cart'),
    path('cartitems/<int:order_id>/', CartDetailView.as_view(), name='api-cartdetail'),
    path('deletecart/<int:cart_id>', CartDeleteView.as_view(), name='api-deletecart'),
    path('ctrl_order/<int:item_id>', OrderControlAPIView.as_view(), name='api-ctrl-order'),
    path('order/<int:order_id>', OrderDetailView.as_view(), name='api-order'),
   
]