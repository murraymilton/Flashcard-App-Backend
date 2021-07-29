from django.http import Http404
from .models import Collections, Cards
from .serializers import CollectionSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CollectionList(APIView):


    def get(self, request):
        collection = Collections.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardCollectionDetail(APIView):

    def get_object(self, pk):
        try:
            return Collections.objects.get(id=pk)
        except Collections.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        collection.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CardsInCollection(APIView):

    def get(self, request, fk):
        card = Cards.objects.filter(collection_id=fk)
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)


class EditCard(APIView):

    def get_object(self, pk):
        try:
            return Cards.objects.get(id=pk)
        except Cards.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        card_id = self.get_object(pk)
        serializer = CardSerializer(card_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        card_id = self.get_object(pk)
        serializer = CardSerializer(card_id)
        card_id.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)