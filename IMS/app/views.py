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
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
   
    
    def list(self,request):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class VendorView(GenericViewSet):    
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
    def list(self,reqeust):
        vendor_obj = self.get_queryset()
        serializer = self.get_serializer(vendor_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class SellView(GenericViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    
    def list(self,request):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class DepartmentView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
    def list(self,request):
        purchase_obj = self.get_queryset()
        serializer = self.get_serializer(purchase_obj,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


