from django.shortcuts import render
from .models import ProductType,Product,Purchase,Vendor,Sell,Department
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .seriallizers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, DepartmentSerializer, VendorSerializer, SellSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class productTypeView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class ProductView(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self,request):
        product_objs = self.get_queryset()
        serializer = self.get_serializer(product_objs,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:                                            #if request is sent from user you must send response
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)       



class PurchaseView(GenericViewSet):
    questyset = Purchase.objects.all()
    serizlizer_class = PurchaseSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


class VendorView(GenericViewSet):
    
    questyset = Vendor.objects.all()
    serizlizer_class = VendorSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


class SellView(GenericViewSet):
    questyset = Sell.objects.all()
    serizlizer_class = SellSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


class DepartmentView(GenericViewSet):
    questyset = Department.objects.all()
    serizlizer_class = DepartmentSerializer
    
    def list(self,reqeust):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


