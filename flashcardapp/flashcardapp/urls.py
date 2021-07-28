from django.urls import path
from . import views

urlpatterns = [
    path('cards/collections', views.CollectionList.as_view()),
    path('cards/collections/info/<int:pk>', views.EditCollection.as_view()),
    path('cards/Collections/collect_collection/<int:fk>', views.CardsCollection.as_view()),
    path('cards/Collections/edit_card/<int:pk>', views.EditCard.as_view())
]
