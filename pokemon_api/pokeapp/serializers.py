from rest_framework import serializers

from pokeapp.models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["name", "id"]
class PokemonSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    def get_type(self, obj):
        return obj.type.name

    class Meta:
        model = Pokemon
        fields = ["id", "name", "number", "type"]
