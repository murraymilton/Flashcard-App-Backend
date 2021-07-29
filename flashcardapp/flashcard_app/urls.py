from django.urls import path
from . import views

urlpatterns = [
    path('cards/collections', views.CollectionList.as_view()),
    path('cards/collections/details/<int:pk>', views.CardCollectionDetail.as_view()),
    path('cards/details/<int:fk>', views.CardsInCollection.as_view()),
    path('cards/editcard/<int:pk>', views.EditCard.as_view())
]
