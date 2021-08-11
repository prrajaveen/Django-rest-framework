from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Student

#function base validator
def one_chracter_in_upper(value):
    if value[0]==value[0].upper():
        return value
    raise serializers.ValidationError('First latter shoud be in uppercase')
        

#order to cheak validiation in serialization
#function or class validator
#field level validator
#object level validator



class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100, validators=[one_chracter_in_upper])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
        
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll', instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance



    #Field level validation

    #200 seat avaliable for admission
    def validate_roll(self,validated_data):
        # print(type(validated_data))
        if validated_data<=200:
            return validated_data
        raise serializers.ValidationError('seat Full')


    #name must be 10 chracter or more
    def validate_name(self,validated_data):
        print(validated_data)
        if len(validated_data)>=10:
            return validated_data
        raise serializers.ValidationError('Name must be 10 character ')


    #object level validation

    def validate(self, data):
        print('hello')
        nm=data.get('name')
        ct=data.get('city')
        if nm()==item.upper():
            return data
        raise serializers.ValidationError('one character must be in uppercase')
        
        
    
            
