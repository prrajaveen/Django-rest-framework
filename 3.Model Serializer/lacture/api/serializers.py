from django.db.models import fields
from django.urls.base import clear_script_prefix
from rest_framework import serializers
from .models import Student

#validators
# def one_chracter_in_upper(value):
#     if not value[0]==value[0].upper():
#         raise serializers.ValidationError('First latter shoud be in uppercase')  
#     return value


class StudentSerializer(serializers.ModelSerializer):
    #update method not work imp****
    # roll=serializers.IntegerField(validators=[roll_no_in_numeric])
    # city=serializers.CharField(max_length=100)
    class Meta:
        model=Student
        fields=['name','roll','city']
        #imp****
        # read_only_fields= ['name' , 'roll']
        # extra_kwargs={'name':{'read_only':True}}

    #field level validation
    def validate_roll(self,value):
        print(type(value))
        if value <= 200:
            return value
        raise serializers.ValidationError('Seat Full')
    
    def validate(self, value):
        name=value.get('name')
        if name[0] == name[0].upper():
            return value
        raise serializers.ValidationError('not valid')
