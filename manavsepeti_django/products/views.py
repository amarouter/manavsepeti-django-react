from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
# from .products import products
from .serializers import ProductSerializer


# Create your views here.

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = None
    try:
        product = Product.objects.get(pk=pk)
    except:
        # is generally Product.DoesNotExist
        pass

    serializer = ProductSerializer(product, many=False) if product else None

    data = serializer.data if serializer else None
    return Response(data)
