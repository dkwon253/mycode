#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    pokeInput = input("What Pokemon do you want to look up? ")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokeInput.lower()).json()

    print(pokeapi["sprites"]["front_default"])

    print("# of games: ", len(pokeapi.get("game_indices")))

    #print moves
    for move_collection in pokeapi.get("moves"):
        print("", move_collection.get('move').get('name'))

main()
