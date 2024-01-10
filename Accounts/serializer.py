from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name','email', 'password']
        
    def create(self, validated_data):
        validated_data['email'] = validated_data.get('email').lower()
        user = UserModel.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()

        return user