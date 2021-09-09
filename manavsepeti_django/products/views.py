from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products


# Create your views here.

@api_view(['GET'])
def get_products(request):
    return Response(products)

@api_view(['GET'])
def get_product(request, pk):
    product = None
    for element in products:
        if element['_id'] == pk:
            product = element
            break
    return Response(product)
