from django.contrib.auth.models import User, Group
from rest_framework import serializers
from shoestore.models import Shoe, ShoeColor, ShoeType, Manufacturer

class ShoeSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(many=False)
    manufacturer = serializers.StringRelatedField(many=False)
    shoe_type = serializers.StringRelatedField(many=False)
    class Meta:
        model = Shoe
        fields = [
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type', 
            'fasten_type'
        ]

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'name',
            'website',
        ]


class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ShoeType
        fields = [
            'style'
        ]

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color'
        ]
