from django.shortcuts import render
from .models import Note
from .serializer import noteserializers ,RegisterSerializer
from rest_framework import generics
from .permissions import IsOwner
from django.contrib.auth.models import User

class Reister(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class = RegisterSerializer


class WriteNote(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class=noteserializers
    

class CrudNote(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class=noteserializers
    permission_classes=[IsOwner]
