from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from rest_framework import status
from product.serializers import ProductSerializer,CategorySerializer
from django.db.models import Count



@api_view()
def view_product(request):
    product=Product.objects.select_related("category").all()
    serializer= ProductSerializer(product, many=True,context={'request': request})
    return Response(serializer.data)

@api_view()
def view_specific_product(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer =ProductSerializer(product)
    # product_dict ={"id":product.id,"name":product.name,"price":product.price} it serializer
    return Response(serializer.data)



@api_view()
def view_category(request):
    category=Category.objects.annotate(product_count=Count("products")).all()
    serializer= CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    serializer =CategorySerializer(category)
    return Response(serializer.data)
    