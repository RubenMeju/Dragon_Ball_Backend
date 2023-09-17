from rest_framework import generics
from .models import Character, Planet, Transformation
from .serializers import CharacterSerializer, PlanetSerializer, TransformationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework.throttling import UserRateThrottle
from django.http import JsonResponse
import django_filters

import os
from dotenv import load_dotenv

load_dotenv()
# Vista para el frontend sin limitar las peticiones


@extend_schema(exclude=True)
class CharacterListDocView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterFilter(django_filters.FilterSet):
    # icontains para búsqueda parcial insensible
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Character
        fields = ['name', 'race']


# Vista para listar personajes (Character)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CharacterFilter  # Usamos la clase de filtro personalizado


# vista para listar personaje por id
class CharacterDetailIdView(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

# Vista para crear personajes (Character)


@extend_schema(exclude=True)
class CharacterCreateView(generics.CreateAPIView):
    throttle_classes = [UserRateThrottle]
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

# Vista para ver, actualizar y eliminar un personaje específico (Character)
# @extend_schema(exclude=True)
# class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer

# Vista para listar planetas (Planet)


class PlanetListView(generics.ListAPIView):
    throttle_classes = [UserRateThrottle]
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

# Vista para crear planetas (Planet)


@extend_schema(exclude=True)
class PlanetCreateView(generics.CreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

# Vista para ver, actualizar y eliminar un planeta específico (Planet)


@extend_schema(exclude=True)
class PlanetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

# Vista para listar y crear transformaciones (Transformation


class TransformationListCreateView(generics.ListCreateAPIView):
    queryset = Transformation.objects.all()
    serializer_class = TransformationSerializer

# Vista para ver, actualizar y eliminar una transformación específica (Transformation)


@extend_schema(exclude=True)
class TransformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transformation.objects.all()
    serializer_class = TransformationSerializer
