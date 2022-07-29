from rest_framework import serializers

from todo.models import Tache, Category




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'slug', 'description', 'complet', 'color', 'image', 'archived', 'taches', 'created', 'updated']


class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = ['url', 'name', 'slug', 'description', 'complet', 'color', 'category', 'created', 'updated']
