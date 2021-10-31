import peewee as pw

database = pw.SqliteDatabase("database.db")


class Chat(pw.Model):
    _id = pw.IntegerField(pk=True)
    id = pw.IntegerField(unique=True)

    class Meta:
        database=database


class ChatMessage(pw.Model):
    peer = pw.ForeignKeyField(Chat, backref="messages", to_field="id")
    message = pw.TextField()

    class Meta:
        database=database


Chat.create_table()
ChatMessage.create_table()
