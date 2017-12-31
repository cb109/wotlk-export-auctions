import sys
import time
from datetime import datetime

import click
from peewee import DoesNotExist
from peewee import Using

from . import db

epoch = datetime.utcfromtimestamp(0)


@click.command()
@click.option("-h", "--host", default="127.0.0.1",
              help="MySQL host (default: 127.0.0.1)")
@click.option("-p", "--port", default=3306, help="MySQL port (default: 3306)")
@click.option("-u", "--user", required=True, help="MySQL user")
@click.option("-P", "--password", required=True, help="MySQL password")
@click.option("-o", "--outfile", type=click.File(mode="w", encoding="utf-8"),
              help="File to save exported data to")
@click.option("-L", "--locale", type=click.Choice(["deDE", "esES", "esMX",
                                                   "frFR", "koKR", "ruRU",
                                                   "zhCN", "zhTW"]),
              help=("If specified, use this locale to translate item names "
                    "(default is english)"))
def cli(host, port, user, password, outfile, locale):
    start = time.time()
    init_databases(host, port, user, password)
    data = query(locale)
    from pprint import pprint; pprint(data)
    stop = time.time()
    sys.stdout.write("===\n Export took: {0:.2f} seconds\n"
                     .format(stop - start))


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
    db.characters_db.init("characters", host=host, port=port,
                          user=user, password=password)
    db.world_db.init("world", host=host, port=port,
                     user=user, password=password)


def datetime_to_epoch_ms(dt):
    return (dt - epoch).total_seconds() * 1000.0


def get_current_auctions():
    """Return auctions that are not yet expired.

    WoW removes expired auctions by itself during AH interactions, but
    it doesn't hurt to also filter here, to ensure we won't list old
    auctions by accident.
    """
    now = datetime_to_epoch_ms(datetime.now())
    auctions = db.Auctionhouse.select().where(db.Auctionhouse.time >= now)
    return auctions


def get_character_name_by_id(character_id):
    try:
        return db.Characters.get(guid=character_id).name
    except DoesNotExist:
        return None


def get_serialized_item_by_id(item_id, locale=None):
    try:
        instance = db.ItemInstance.get(guid=item_id)
        template = db.ItemTemplate.get(entry=instance.itementry)
        template_name = template.name
        if locale is not None:
            template_name = db.ItemTemplateLocale.get(id=instance.itementry,
                                                      locale=locale).name
        return {
            "id": template.entry,
            "count": instance.count,
            "quality": template.quality,
            "name": template_name,
            "requiredlevel": template.requiredlevel
        }
    except DoesNotExist:
        return None


if __name__ == "__main__":
    cli(auto_envvar_prefix="EXPORT_AUCTIONS")
