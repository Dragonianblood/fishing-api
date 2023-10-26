from random import randint
from fastapi import APIRouter

fish = {'swordfish': {'weight': 50, 'population': 5000, 'life_span': 49},
        'salmon': {'weight': 10, 'population': 5000, 'life_span': 6},
        'tilapia': {'weight': 2, 'population': 5000, 'life_span': 9},
        'cod': {'weight': 5, 'population': 5000, 'life_span': 3},
        'anchovies': {'weight': 1, 'population': 5000, 'life_span': 24},
        'halibut': {'weight': 8, 'population': 5000, 'life_span': 5},
        'catfish': {'weight': 23, 'population': 5000, 'life_span': 2},
        'mahi-mahi': {'weight': 14, 'population': 5000, 'life_span': 14},
        'betta': {'weight': 5, 'population': 5000, 'life_span': 8},
        'flounder': {'weight': 14, 'population': 5000, 'life_span': 9},
        'guppi': {'weight': 2, 'population': 5000, 'life_span': 4},
        'bass': {'weight': 6, 'population': 5000, 'life_span': 27},
        'goldfish': {'weight': 2, 'population': 5000, 'life_span': 8},
        'tuna': {'weight': 11, 'population': 5000, 'life_span': 31},
        'sardine': {'weight': 1, 'population': 5000, 'life_span': 1},
        'trout': {'weight': 9, 'population': 5000, 'life_span': 7},
        'pike': {'weight': 4, 'population': 5000, 'life_span': 4},
        'carp': {'weight': 3, 'population': 5000, 'life_span': 9000},
        'perch': {'weight': 16, 'population': 5000, 'life_span': 4},
        'barracuda': {'weight': 39, 'population': 5000, 'life_span': 23}}

keys = ['4675636B20796F75']
router = APIRouter()

# Here we see that order matters. Going to this path will trigger this route first rather than the next because it
# comes first

@router.get("/fishes")
async def intake(api_key: str):
    for key in keys:
        if key == api_key:
            global fish
            fish_names = []
            for fishes in fish:
                fish_names.append(fishes)
            return fish_names
        else:
            return f'ERROR:Invalid API key'
@router.get("/catch")
async def newest_catch(api_key: str):
    for key in keys:
        if key == api_key:
            global fish
            num = 0
            compare = randint(0, 19)
            for fishes in fish:
                if compare == num:
                    weight = fish[fishes]['weight']
                    return {'name':fishes, 'weight': randint(weight * 8, weight * 12) / 10}
                num += 1
        else:
            return f'ERROR:Invalid API key'

@router.get("/info/{fish_type}")
def info(fish_type: str, api_key: str):
    for key in keys:
        if key == api_key:
            global fish
            population = fish[fish_type]['population']
            return {'population': randint(population * 8, population * 12), 'lifespan': fish[fish_type]["life_span"]}
        else:
            return f'ERROR:Invalid API key'
