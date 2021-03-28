from .db import Database
from peewee import Model
import peewee


class Base(Model):
    class Meta:
        database = Database


class Chat(Base):
    peer = peewee.IntegerField(unique=True)


class ChatMessage(Base):
    chat = peewee.ForeignKeyField(Chat)
    message = peewee.TextField()
