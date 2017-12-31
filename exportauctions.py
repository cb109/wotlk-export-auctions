"""
Export current auction house data to JSON.

Usage: exportauctions.py [OPTIONS]

Options:
  -h, --host TEXT                 MySQL host (default: 127.0.0.1)
  -p, --port INTEGER              MySQL port (default: 3306)
  -u, --user TEXT                 MySQL user  [required]
  -P, --password TEXT             MySQL password  [required]
  -o, --outfile FILENAME          File to save exported data to
  -L, --locale [deDE|esES|esMX|frFR|koKR|ruRU|zhCN|zhTW]
                                  If specified, add the translated item name
                                  to the result (english is always included)
  --help                          Show this message and exit.

"""
import json
from datetime import datetime
from pprint import pprint

import click
from peewee import CharField
from peewee import CompositeKey
from peewee import DoesNotExist
from peewee import IntegerField
from peewee import Model
from peewee import MySQLDatabase
from peewee import PrimaryKeyField
from peewee import TextField


epoch = datetime.utcfromtimestamp(0)

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


@click.command()
@click.option("-h", "--host", default="127.0.0.1",
              help="MySQL host (default: 127.0.0.1)")
@click.option("-p", "--port", default=3306, help="MySQL port (default: 3306)")
@click.option("-u", "--user", required=True, help="MySQL user")
@click.option("-P", "--password", required=True, help="MySQL password")
@click.option("-o", "--outfile", type=click.File(mode="w", atomic=True),
              help="File to save exported data to")
@click.option("-L", "--locale", default="deDE", type=click.Choice([
    "deDE", "esES", "esMX", "frFR", "koKR", "ruRU", "zhCN", "zhTW"]),
    help=("If specified, add the translated item name to the result "
          "(english is always included)"))
def cli(host, port, user, password, outfile, locale):
    init_databases(host, port, user, password)
    data = query(locale)
    if outfile is None:
        pprint(data)
    else:
        outfile.write(json.dumps(data, indent=4, encoding="utf-8"))


def query(locale):
    data = {
        "auctions": [],
        "locale": locale,
        "time": datetime_to_epoch_ms(datetime.now()),
    }

    auctions = get_current_auctions()
    for auction in auctions:
        serialized_auction = {
            "id": int(auction.id),
            "houseid": int(auction.id),
            "item": get_serialized_item_by_id(auction.itemguid, locale=locale),
            "owner": {
                "name": get_character_name_by_id(auction.itemowner),
            },
            "buyoutprice": auction.buyoutprice,
            "deposit": auction.deposit,
            "lastbid": auction.lastbid,
            "startbid": auction.startbid,
            "time": auction.time,
        }
        data["auctions"].append(serialized_auction)

    return data


def init_databases(host, port, user, password):
    characters_db.init("characters", host=host, port=port, user=user,
                       password=password)
    world_db.init("world", host=host, port=port, user=user, password=password)


def datetime_to_epoch_ms(dt):
    return (dt - epoch).total_seconds() * 1000.0


def get_current_auctions():
    """Return auctions that are not yet expired.

    WoW removes expired auctions by itself during AH interactions, but
    it doesn't hurt to also filter here, to ensure we won't list old
    auctions by accident.
    """
    now = datetime_to_epoch_ms(datetime.now())
    auctions = Auctionhouse.select().where(Auctionhouse.time >= now)
    return auctions


def get_character_name_by_id(character_id):
    try:
        return Characters.get(guid=character_id).name
    except DoesNotExist:
        return None


def get_serialized_item_by_id(item_id, locale=None):
    try:
        instance = ItemInstance.get(guid=item_id)
        template = ItemTemplate.get(entry=instance.itementry)
        template_name = template.name
        data = {
            "id": template.entry,
            "count": instance.count,
            "quality": template.quality,
            "name": template_name,
            "requiredlevel": template.requiredlevel
        }
        if locale is not None:
            locale_name = ItemTemplateLocale.get(id=instance.itementry,
                                                 locale=locale).name
            data["locale_name"] = locale_name
        return data
    except DoesNotExist:
        return None


if __name__ == "__main__":
    cli()
