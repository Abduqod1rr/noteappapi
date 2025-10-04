from rest_framework import serializers
from .models import Note

class noteserializers(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=['id','title','text']