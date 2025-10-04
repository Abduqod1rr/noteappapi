from django.shortcuts import render
from .models import Note
from .serializer import noteserializers
from rest_framework import generics
from .permissions import IsOwner
# Create your views here.

class WriteNote(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class=noteserializers
    

class CrudNote(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class=noteserializers
    permission_classes=[IsOwner]
