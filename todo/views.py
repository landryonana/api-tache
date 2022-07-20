from django.shortcuts import render
from rest_framework import viewsets
from todo.models import Category, Tache
from todo.serializers import CategorySerializer, TacheSerializer



class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TacheViewset(viewsets.ModelViewSet):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer
