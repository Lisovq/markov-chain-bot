from typing import Union, List

from models.db import Manager
from peewee import Model


class BaseRepository(object):
    model: Model = None

    async def filter(self, *args, **kw) -> List["Model"]:
        args = list(args) + self.__convert_args(**kw)
        query = self.model.select().where(*args)
        return await Manager.execute(query)

    async def get(self, *args, **kw) -> Union["Model", None]:
        query = self.model.select()
        if args: query.where(*args)
        try:
            return await Manager.get(query, **kw)
        except self.model.DoesNotExist:
            return None

    async def create(self, **params) -> tuple:
        return await Manager.create(self.model, **params)

    async def get_or_create(self, **kw):
        return await self.get(*self.__convert_args(**kw)) or await self.create(**kw)

    async def delete(self, *objects):
        {await Manager.delete(obj) for obj in objects}

    def __convert_args(self, **kw):
        return [getattr(self.model, k) == v for k, v in kw.items()]
