from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token

from pokeapp.models import Pokemon, Type
from pokeapp.serializers import PokemonSerializer, TypeSerializer
from pokeapp.forms import PokemonForm, TypeForm
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def pokelist(request):
    pokes = get_all_pokemon()
    return render(request, "pokelist.html", {"pokes": pokes})

def typelist(request):
    types = get_all_types()
    return render(request, "typelist.html", {"types": types})

def get_all_types():
    types = Type.objects.all().order_by("name")
    types_serializer = TypeSerializer(types, many=True)
    return types_serializer.data

def get_all_pokemon():
    pokes = Pokemon.objects.all().order_by("number")
    pokes_serializer = PokemonSerializer(pokes, many=True)
    return pokes_serializer.data
    # pokes_data = []
    # for poke in pokes:
    #     poke_data = {
    #         "id": poke.id,
    #         "name": poke.name,
    #         "number": poke.number,
    #         "type": poke.type.name
    #     }
    #     pokes_data.append(poke_data)
    # return pokes_data
def add_pokemon_form(request):
    if request.method == "POST":
        pokemon_form = PokemonForm(request.POST)
        if pokemon_form.is_valid():
            poke = pokemon_form.save()
            return HttpResponseRedirect("pokelist")
    if request.method == "GET":
        pokemon_form = PokemonForm()
        csrf_token = get_token(request)
        html_form = f"""
            <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                {pokemon_form.as_p()}
                <button type="submit">Submit</button>
            </form>
        """
        return HttpResponse(html_form)
def add_type_form(request):
    if request.method == "POST":
        type_form = TypeForm(request.POST)
        if type_form.is_valid():
            type = type_form.save()
            return HttpResponseRedirect("typelist")
    if request.method == "GET":
        type_form = TypeForm()
        csrf_token = get_token(request)
        html_form = f"""
            <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                {type_form.as_p()}
                <button type="submit">Submit</button>
            </form>
        """
        return HttpResponse(html_form)
