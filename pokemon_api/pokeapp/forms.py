from django import forms
from pokeapp.models import Pokemon, Type

class TypeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"name": "Type name"}))
    class Meta:
        model = Type
        fields = [
            "name"
        ]

class PokemonForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Pokemon name"}))
    number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Pokedex number"}))
    queryset = Type.objects.all()
    type = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={"class": "main type"}), to_field_name="name")
    class Meta:
        model = Pokemon
        fields = [
            "name",
            "number",
            "type"
        ]
