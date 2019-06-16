import typing

import databases
import orm
import sqlalchemy
from hashids import Hashids

from . import settings

hashids = Hashids()
database = databases.Database(str(settings.DATABASE_URL))
metadata = sqlalchemy.MetaData()


class LinkQuerySet(orm.models.QuerySet):
    async def get_or_create(self, **kwargs) -> typing.Tuple["Link", bool]:
        try:
            link = await self.get(**kwargs)
        except orm.NoMatch:
            link = await self.create(**kwargs)
            await link.update(hash=hashids.encode(link.pk))
            created = False
        else:
            created = False
        return link, created


class Link(orm.Model):
    __tablename__ = "links"
    __database__ = database
    __metadata__ = metadata
    objects = LinkQuerySet()

    id = orm.Integer(primary_key=True)
    url = orm.String(max_length=300)
    hash = orm.String(max_length=20, allow_null=True)


engine = sqlalchemy.create_engine(str(settings.DATABASE_URL))
metadata.create_all(engine)
