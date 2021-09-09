from django.http import JsonResponse


# Create your views here.

def get_routes(request):
    routes = [
        '/api/v1/products',
        '/api/v1/products/<id>',
        '/api/v1/products/create',
        '/api/v1/products/delete/<id>',
        '/api/v1/products/<update>/<id>',
        '/api/v1/products/upload',
        '/api/v1/products/<id>/reviews',
        '/api/v1/products/top',
    ]
    return JsonResponse(routes, safe=False)
