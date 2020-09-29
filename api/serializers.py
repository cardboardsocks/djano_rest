from django.contrib.auth.models import User, Group
from rest_framework import serializers
from shoestore.models import Shoe

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