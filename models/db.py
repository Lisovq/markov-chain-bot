import peewee_async

Database = peewee_async.PostgresqlDatabase(
    "test_markov_bot"
)
Database.allow_sync()

Manager = peewee_async.Manager(Database)
