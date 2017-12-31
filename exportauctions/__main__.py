from datetime import datetime

import click

from . import db


epoch = datetime.utcfromtimestamp(0)


@click.command()
@click.option("-h", "--host", default="127.0.0.1",
              help="MySQL host (default: 127.0.0.1)")
@click.option("-p", "--port", default=3306, help="MySQL port (default: 3306)")
@click.option("-u", "--user", required=True, help="MySQL user")
@click.option("-P", "--password", required=True, help="MySQL password")
@click.option("-l", "--locale", type=click.Choice(["deDE", "esES", "esMX",
                                                   "frFR", "koKR", "ruRU",
                                                   "zhCN", "zhTW"]),
              help=("If specified, use this locale to translate item names "
                    "(default is english)"))
def cli(host, port, user, password, locale):
    init_databases(host, port, user, password)
    data = query()


def query():
    auctions = get_current_auctions()


def init_databases(host, port, user, password):
    db.characters_db.init("characters", host=host, port=port,
                          user=user, password=password)
    db.world_db.init("characters", host=host, port=port,
                     user=user, password=password)


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0


def get_current_auctions():
    """Return auctions that are not yet expired.

    WoW removes expired auctions by itself during AH interactions, but
    it doesn't hurt to also filter here, to ensure we won't list old
    auctions by accident.
    """
    now = unix_time_millis(datetime.now())
    auctions = db.Auctionhouse.select().where(db.Auctionhouse.time >= now)
    return auctions


if __name__ == "__main__":
    cli(auto_envvar_prefix="EXPORT_AUCTIONS")
