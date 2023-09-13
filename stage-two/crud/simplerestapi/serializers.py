from rest_framework import serializers
from .models import Person
import bleach
from rest_framework.validators import UniqueValidator

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']
        
    def validate_name(self, value):
        return bleach.clean(value)
    
    def to_internal_value(self, data): 
        if 'name' in data and not isinstance(data['name'], str):
            raise serializers.ValidationError({'name': ['Name must be a string']})
        return super().to_internal_value(data)