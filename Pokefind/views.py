from django.shortcuts import render
import requests

def search_pokemon(request):
    pokemon_data = None
    if request.method == 'POST':
        # Corrected line
        query = request.POST.get('pokemon_name').lower()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query}')
        if response.status_code == 200:
            pokemon_data = response.json()
        else:
            pokemon_data = {'error': 'Pokémon not found'}
    
    return render(request, 'pokemon_search.html', {'pokemon_data': pokemon_data})
