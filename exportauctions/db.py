from peewee import CharField
from peewee import CompositeKey
from peewee import IntegerField
from peewee import Model
from peewee import MySQLDatabase
from peewee import PrimaryKeyField
from peewee import TextField


# http://docs.peewee-orm.com/en/latest/peewee/database.html#run-time-database-configuration  # noqa
characters_db = MySQLDatabase(None)
world_db = MySQLDatabase(None)


class CharactersBaseModel(Model):
    class Meta:
        database = characters_db


class WorldBaseModel(Model):
    class Meta:
        database = world_db


class Characters(CharactersBaseModel):
    guid = PrimaryKeyField()
    name = CharField(index=True)

    class Meta:
        db_table = "characters"


class Auctionhouse(CharactersBaseModel):
    buyguid = IntegerField()
    buyoutprice = IntegerField()
    deposit = IntegerField()
    houseid = IntegerField()
    itemguid = IntegerField(unique=True)
    itemowner = IntegerField()
    lastbid = IntegerField()
    startbid = IntegerField()
    time = IntegerField()

    class Meta:
        db_table = "auctionhouse"


class ItemInstance(CharactersBaseModel):
    count = IntegerField()
    guid = PrimaryKeyField()
    itementry = IntegerField(db_column="itemEntry")

    class Meta:
        db_table = "item_instance"


class ItemTemplate(WorldBaseModel):
    quality = IntegerField(db_column="Quality")
    requiredlevel = IntegerField(db_column="RequiredLevel")
    entry = PrimaryKeyField()
    name = CharField(index=True)

    class Meta:
        db_table = "item_template"


class ItemTemplateLocale(WorldBaseModel):
    id = IntegerField(db_column="ID")
    name = TextField(db_column="Name", null=True)
    locale = CharField()

    class Meta:
        db_table = "item_template_locale"
        indexes = (
            (("id", "locale"), True),
        )
        primary_key = CompositeKey("id", "locale")
