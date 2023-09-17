from django.db import models
import os
from django.conf import settings
from PIL import Image
def character_image_path(instance, filename):
    character_name = instance.character.name
    return os.path.join('transformations', character_name, filename)

class Planet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Transformation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Character(models.Model):
    gender_choices = [
        ('FE', 'Mujer'),
        ('MA', 'Hombre'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=165)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    image = models.ImageField(upload_to="characters")
    gender = models.CharField(max_length=2, choices=gender_choices)

    planet_origin = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, related_name='born_characters')
    planet_current = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, related_name='current_residents')

    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True, related_name='race')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image:
            # Abrir la imagen principal utilizando Pillow
            img = Image.open(self.image.path)
            
            # Redimensionar la imagen para crear la miniatura
            thumbnail_size = (100, 100)  # Tamaño de la miniatura
            img.thumbnail(thumbnail_size)
            
            # Obtener la extensión del archivo original
            file_extension = os.path.splitext(self.image.name)[1]
            
            # Construir el nombre del archivo de la miniatura
            thumbnail_name = f"{os.path.basename(self.image.name).replace(file_extension, '')}_thumbnail{file_extension}"
            
            # Obtener la ruta completa para guardar la miniatura
            thumbnail_path = os.path.join(settings.MEDIA_ROOT, f"thumbnails/{thumbnail_name}")
            
            # Verificar si la carpeta thumbnails existe y crearla si no
            thumbnail_folder = os.path.dirname(thumbnail_path)
            os.makedirs(thumbnail_folder, exist_ok=True)
            
            # Crear y guardar la miniatura en la ruta completa
            img.save(thumbnail_path)
            
            # Asignar la miniatura al campo correspondiente
            self.thumbnail = thumbnail_path.replace(settings.MEDIA_ROOT, "")  # Guardar ruta relativa en el campo
            super().save(*args, **kwargs)  # Guardar nuevamente para actualizar el campo thumbnail

class TransformationCharacter(models.Model):
    transformation = models.ForeignKey(Transformation, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=character_image_path)
    description = models.TextField(max_length=165)

    def __str__(self):
        return f"{self.character.name} - {self.transformation.name}"
