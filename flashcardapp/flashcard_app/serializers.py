from rest_framework import serializers
from .models import Collections, Cards


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ['id', 'name', 'description']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ['id', 'question', 'answer', 'collection']