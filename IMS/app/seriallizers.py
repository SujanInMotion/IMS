from rest_framework import serializers
from .models import ProductType,Product,Purchase,Vendor,Sell,Department
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
        
class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'
        
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
        
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    #group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False)
    class Meta:
        model = User
        # fields = ['username','password']
        fields = ['username','password','groups']
        
        
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }
        
class UserSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

        
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']
        
        
    
        