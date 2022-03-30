from rest_framework import serializers
from fruits.models import Region, Fruit 

class FruitSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = Fruit        
        fields = "__all__"  
class RegionSerializer(serializers.ModelSerializer):    
    fruits = FruitSerializer(many=True, read_only=True)      
    class Meta:        
        model = Region         
        fields = ("name","fruits","id",)