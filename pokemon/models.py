from pokemon.extension import db, LoginManager
from sqlalchemy import Integer, Text, String, DateTime, ForeignKey, Column, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from datetime import datetime
from flask_login import UserMixin

@LoginManager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  username: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(String(255), nullable=False)
  firstname: Mapped[str] = mapped_column(String(25), nullable=True)
  lastname: Mapped[str] = mapped_column(String(25), nullable=True)
  avatar: Mapped[str] = mapped_column(String(255), nullable=True,default='avatar.png')
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
  
  pokemons: Mapped[List['Pokemon']] = relationship(back_populates='user', cascade='all, delete-orphan')
  def __repr__(self):
    return f'<User {self.username}>'

pokedex = Table('pokedex',
      db.metadata,
      Column('type_id', Integer, ForeignKey('types.id'), primary_key=True),
      Column('pokemon_id' , Integer, ForeignKey('pokemon.id'), primary_key=True)
      )

class Type(db.Model):
  __tablename__ = 'types'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)

  pokemons: Mapped[List['Pokemon']] = relationship('Pokemon', secondary=pokedex, back_populates='types')

  def __repr__(self):
    return f'<Type {self.name}>'

class Pokemon(db.Model):
  __tablename__ = 'pokemon'
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
  height: Mapped[str] = mapped_column(String(15), nullable=False)
  weight: Mapped[str] = mapped_column(String(15), nullable=False)
  description: Mapped[str] = mapped_column(Text, nullable=False)
  img_url: Mapped[str] = mapped_column(String(255), nullable=False)
  user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

  user: Mapped['User'] = relationship(back_populates='pokemons')
  types: Mapped[List['Type']] = relationship(secondary=pokedex, back_populates='pokemons')
  def __repr__(self):
    return f'<Pokemon {self.name}>'

