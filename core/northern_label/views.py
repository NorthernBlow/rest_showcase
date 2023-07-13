from rest_framework.response import Response
from northern_label.models import Category, Brand, Product, Cart, User
from rest_framework import generics, viewsets, status
from northern_label.serializers import CategorySerializer, BrandSerializer, ProductSerializer, CategoryPagination, CartSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from .helpers import CartHelper




class CategoryAPIView(generics.ListAPIView):
    """
    A simple set for viewing all categories
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class BrandAPIView(generics.ListAPIView):
    """
    A simple set for viewing all brands
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = CategoryPagination



class ProductViewSet(viewsets.ViewSet):
    """
    Viewset to view all products
    """

    queryset = Product.objects.all()
    pagination_class = CategoryPagination

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer





class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save()


    @action(methods=['get'], detail=False, url_path='checkout/(?P<userId>[^/.]+)', url_name='checkout')
    def checkout(self, request, *args, **kwargs):

        try:
            user = User.objects.get(pk=int(kwargs.get('userId')))
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'Error': str(e)})
        cart_helper = CartHelper(user)
        checkout_details = cart_helper.prepare_cart_for_checkout()

        if not checkout_details:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'error': 'Cart of user is empty.'})

        return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})
