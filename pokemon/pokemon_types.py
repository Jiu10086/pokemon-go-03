from sqlalchemy import select

from pokemon.models import Type


DEFAULT_TYPES = [
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


def ensure_pokemon_types(session):
  existing_names = set(session.scalars(select(Type.name)).all())
  missing_types = [Type(name=pt) for pt in DEFAULT_TYPES if pt not in existing_names]

  if missing_types:
    session.add_all(missing_types)
    session.commit()