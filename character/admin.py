from django.contrib import admin
from .models import Character, Planet, Transformation, TransformationCharacter, Race


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'gender',
                    'planet_origin', 'planet_current')
    list_filter = ('race', 'gender', 'planet_origin', 'planet_current')
    search_fields = ('name', 'race__name', 'gender',
                     'planet_origin__name', 'planet_current__name')


class TransformationCharacterAdmin(admin.ModelAdmin):
    list_display = ('id','character', 'transformation', 'image')
    list_filter = ('character', 'transformation')
    search_fields = ('character__name', 'transformation__name')


class TransformationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class RaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Character, CharacterAdmin)
admin.site.register(Planet)
admin.site.register(Transformation, TransformationAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(TransformationCharacter, TransformationCharacterAdmin)
