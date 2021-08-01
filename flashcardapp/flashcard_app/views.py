from django.http import Http404
from .models import Collections, Cards
from .serializers import CollectionSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CollectionList(APIView):

    def get(self, request):
        try:
            collection = Collections.objects.all()
            serializer = CollectionSerializer(collection, many=True)
            return Response(serializer.data)
        except Collections.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardList(APIView):

    def get(self, request):
        try:
            card = Cards.objects.all()
            serializer = CardSerializer(card, many=True)
            return Response(serializer.data)
        except Cards.DoesNotExist:
            raise Http404

    def post(self, request, collection):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CardDetail(APIView):

    def get_object(self, collection):
        try:
            return Cards.objects.filter(collection=collection)
        except Collections.DoesNotExist:
            raise Http404

    def get(self, request, collection):
        try:
            card = self.get_object(collection)
            serializer = CardSerializer(card, many=True)
            return Response(serializer.data)
        except Collections.DoesNotExist:
            raise Http404


class CardEdit(APIView):

    def get_object(self, pk):
        try:
            return Cards.objects.get(pk=pk)
        except Cards.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)