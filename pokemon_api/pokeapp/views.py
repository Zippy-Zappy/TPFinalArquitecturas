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
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <div class="mb-3">
                <form method="post">
                <input type="hidden" class="form-control" name="csrfmiddlewaretoken" value="{csrf_token}">
                    {pokemon_form.as_p()}
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
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
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
            <div class="mb-3">
                <form method="post">
                <input type="hidden" class="form-control" name="csrfmiddlewaretoken" value="{csrf_token}">
                    {type_form.as_p()}
                    <button type="submit" class="btn btn-primary">Submit</button>
                </form>
            </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        """
        return HttpResponse(html_form)
