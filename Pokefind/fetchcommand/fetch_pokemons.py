import requests
from django.core.management.base import BaseCommand
from Pokefind.models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get('https://pokeapi.co/api/v2/pokemon/')
        pokemons = response.json()['results']
        
        for pokemon in pokemons:
            details = requests.get(pokemon['https://pokeapi.co/api/v2/pokemon/']).json()
            Pokemon.objects.create(
                name=details['name'],
                image_url=details['sprites']['front_default'],
                pokemon_type=details['types'][0]['type']['name']
            )
