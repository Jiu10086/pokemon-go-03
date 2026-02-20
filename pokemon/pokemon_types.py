types = [
  'Fire',
  'Water',
  'Bug',
  'Steel',
  'Rock',
  'Fairy',
  'Electric',
  'Dragon',
  'Ghost',
  'Ground',
  'Grass',
  'Fighting',
  'Dark',
  'Poison',
  'Ice',
  'Normal',
  'Psychic',
  'Flying'
]
from pokemon.models import Type
pokemon_types = [Type(name=pt) for pt in types]