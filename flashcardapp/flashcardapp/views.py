from django.http import Http404
from django.shortcuts import render
from flashcardapp.flashcard.models import Collections, Cards
from .serializers import CollectionSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status


class CollectionList(APIView):


    def get(self, request):
        collections = Collections.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditCollection(APIView):

    def get_by_id(self, pk):
        try:
            return Collections.objects.get(pk=pk)
        except Collections.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collections = self.get_by_id(pk)
        serializer = CollectionSerializer(collections)
        return Response (serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        collections = self.get_by_id(pk)
        serializer = CollectionSerializer(collections)
        collections.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardsCollection(APIView):

    def get(self, request, fk ):
        cards = self.get_by_id.filter(Collections=fk)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, fk):
        serializer = CardSerializer(data=request.data, fk=fk)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditCard(APIView):

    def get_card(self, pk):
        try:
            return Cards.objects.get(id=pk)
        except Cards.DoesNotExist:
            raise Http404

    def add(self, request, pk):
        card = self.get_card(pk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_card(pk)
        serializer = CardSerializer(card)
        card.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)