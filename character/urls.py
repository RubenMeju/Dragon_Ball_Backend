from django.urls import path
from . import views

urlpatterns = [
    path('list-characters-doc/', views.CharacterListDocView.as_view(), name='character-list-doc'),

    path('characters/', views.CharacterListView.as_view(), name='character-list'),
    path('characters/<int:pk>/', views.CharacterDetailIdView.as_view(), name='character-id'),
    path('characters/', views.CharacterCreateView.as_view(), name='character-create'),
    #path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail'),
 
    path('planets/', views.PlanetListView.as_view(), name='planet-list'),
    path('planets/', views.PlanetCreateView.as_view(), name='planet-create'),
    path('planets/<int:pk>/', views.PlanetDetailView.as_view(), name='planet-detail'),
 
    path('transformations/', views.TransformationListCreateView.as_view(), name='transformation-list-create'),
    path('transformations/<int:pk>/', views.TransformationDetailView.as_view(), name='transformation-detail'),
]
