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
        product = Product.objects.get(_id=pk)
    except:
        pass
    
    serializer = None
    if product:
        serializer = ProductSerializer(product, many=False)

    data = serializer.data if serializer else None
    return Response(data)
