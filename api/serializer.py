from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class noteserializers(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=['id','title','text']