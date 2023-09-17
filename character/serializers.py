from rest_framework import serializers
from .models import Character,Planet,Race, Transformation,TransformationCharacter

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Puedes agregar más información al token si lo deseas
        # token['custom_field'] = 'value'

        return token



class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class TransformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformation
        fields = ['id', 'name']

class TransformationCharacterSerializer(serializers.ModelSerializer):
    transformation = TransformationSerializer()

    class Meta:
        model = TransformationCharacter
        fields = ['transformation']

class CharacterSerializer(serializers.ModelSerializer):
    planet_origin = serializers.SlugRelatedField(slug_field='name', queryset=Planet.objects.all())
    planet_current = serializers.SlugRelatedField(slug_field='name', queryset=Planet.objects.all())
    race = serializers.SlugRelatedField(slug_field='name', queryset=Race.objects.all())
    transformations = serializers.SerializerMethodField()
    image = serializers.ImageField()

    class Meta:
        model = Character
        fields = ['id', 'planet_origin', 'planet_current', 'race', 'transformations', 'name', 'description','thumbnail', 'image', 'gender']

    def get_transformations(self, character):
        transformation_characters = TransformationCharacter.objects.filter(character=character)
        serialized_transformations = []

        for tc in transformation_characters:
            transformation_data = TransformationCharacterSerializer(tc).data
            image_url = self.context['request'].build_absolute_uri(tc.image.url)
            description = tc.description
            transformation_data['transformation']['image'] = image_url
            transformation_data['transformation']['description'] = description
            
            # Flatten the "transformation" dictionary
            transformation_data.update(transformation_data.pop('transformation'))

            serialized_transformations.append(transformation_data)

        return serialized_transformations



