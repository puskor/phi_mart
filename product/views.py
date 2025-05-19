from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,Category
from rest_framework import status
from product.serializers import ProductSerializer,CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# -----------------------------------------------------------------------------------------

@api_view(["GET","POST"])
def view_product(request):
    if request.method == "GET":
        product=Product.objects.select_related("category").all()
        serializer= ProductSerializer(product, many=True,context={'request': request})
        return Response(serializer.data)
    if request.method =="POST":
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        return Response("Okay")
    
    
class ViewProduct(APIView):
    def get(self,request):
        product=Product.objects.select_related("category").all()
        serializer= ProductSerializer(product, many=True,context={'request': request})
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        return Response("Okay")
    
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
#  -------------------------------------------------------------------------------------

        

@api_view(["GET","PUT","DELETE"])
def view_specific_product(request,id):
    if request.method=="GET":
        product = get_object_or_404(Product,pk=id)
        serializer =ProductSerializer(product)
        return Response(serializer.data)
    if request.method=="PUT":
        product =get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method=="DELETE":
        product = get_object_or_404(Product,pk=id)
        copy_product=product
        product.delete()
        serializer = ProductSerializer(copy_product)
        return Response(serializer.data,status= status.HTTP_204_NO_CONTENT)
    
class ViewSpecificProduct(APIView):
    def get(self,request,id):
        product = get_object_or_404(Product,pk=id)
        serializer =ProductSerializer(product)
        return Response(serializer.data)
    def put(self,request,id):
        product =get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        product = get_object_or_404(Product,pk=id)
        copy_product=product
        product.delete()
        serializer = ProductSerializer(copy_product)
        return Response(serializer.data,status= status.HTTP_204_NO_CONTENT)
    
class SpecificProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def delete(self,request,pk):
        product =  get_object_or_404(Product,pk=pk)
        if product.stock > 10:
            return Response({"message":"This product stock more then 10 so i cannot delete"})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# -----------------------------------------------------------------------------------------

# class ProductList(ListAPIView):
#     queryset = 

    # if request.method =="POST":
    #     serializer = ProductSerializer(data = request.data)
    #     if serializer.is_valid():
    #         print(serializer)
    #         serializer.save()
    #         return Response("Okay")
    #     else:
    #         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET","POST"])
def view_category(request):
    if request.method=="GET":
        category=Category.objects.annotate(product_count=Count("products")).all()
        serializer= CategorySerializer(category, many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        
class ViewCategory(APIView):
    def get(self,request):
        category=Category.objects.annotate(product_count=Count("products")).all()
        serializer= CategorySerializer(category, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
class CategoryList(ListCreateAPIView):
    queryset=Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = CategorySerializer
    
class CategoryViewset(ModelViewSet):
    queryset=Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = CategorySerializer
    
# -----------------------------------------------------------------------------------------

@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    serializer =CategorySerializer(category)
    return Response(serializer.data)

class ViewSpecificCategory(APIView):
    def get(self,request,pk):
        category = get_object_or_404(Category.objects.annotate(product_count=Count("products")).all(),pk=pk)
        serializer =CategorySerializer(category)
        return Response(serializer.data)
    def put(self,request,pk):
        category = get_object_or_404(Category.objects.annotate(product_count=Count("products")).all(),pk=pk)
        serializer= CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        category = get_object_or_404(Category,pk=pk)
        save_category=category
        category.delete()
        serializer=CategorySerializer(save_category)
        return Response(serializer.data , status=status.HTTP_204_NO_CONTENT)
    
class SpecificCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count("products")).all()
    serializer_class =CategorySerializer



# -----------------------------------------------------------------------------------------
