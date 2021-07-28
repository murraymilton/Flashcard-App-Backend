from django.urls import path
from . import views

urlpatterns = [
    path('collections', views.CollectionList.as_view()),
    path('cards/collections/<int:pk>', views.EditCollection.as_view()),
    path('cards/', views.CardsCollection.as_view()),
    path('cards/<int:pk>', views.EditCard.as_view())
]
