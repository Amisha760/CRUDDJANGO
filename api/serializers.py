from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Student

class StudentSerialzer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=200)
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('name',instance.city)
        instance.save()
        return instance