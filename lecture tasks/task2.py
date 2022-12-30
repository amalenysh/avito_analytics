class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __repr__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    pokemon_to_emoji = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __repr__(self):
        name_and_type = super().__repr__()
        name, pokemon_type = name_and_type.split('/')
        if pokemon_type in self.pokemon_to_emoji:
            return name + '/' + self.pokemon_to_emoji[pokemon_type]
        return name_and_type


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    pikachu = Pokemon(name='Pikachu', poketype='electric')
    print(pikachu)
