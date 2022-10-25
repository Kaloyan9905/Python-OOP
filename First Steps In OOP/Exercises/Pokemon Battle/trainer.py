from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        for pokemon_info in self.pokemons:
            if pokemon_info.name == pokemon.name:
                return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon_info in self.pokemons:
            if pokemon_info.name == pokemon_name:
                self.pokemons.remove(pokemon_info)
                return f"You have released {pokemon_info.name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"

        return result


