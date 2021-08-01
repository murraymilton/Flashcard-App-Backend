from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionList.as_view()), # Will return all/Post Collections
    path('collection/card/', views.CardList.as_view()), # Will return all cards
    path('collection/card/<int:collection>/new/', views.CardList.as_view()),  # Will post Card by Collection ID
    path('collection/card/<int:collection>/', views.CardDetail.as_view()),  # Will get card collection  by Collection ID
    path('collection/card/<int:pk>/update/', views.CardEdit.as_view()),  # Will place the card Card PUT
    path('collection/card/<int:pk>/delete/', views.CardEdit.as_view()),  # Will delete the Card DELETE
]
