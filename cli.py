import click


@click.command()
@click.option("-h", "--host", default="127.0.0.1",
              help="MySQL host (default: 127.0.0.1)")
@click.option("-p", "--port", default=3306, help="MySQL port (default: 3306)")
@click.option("-u", "--user", help="MySQL user")
@click.option("-P", "--password", help="MySQL password")
@click.option("-l", "--locale", type=click.Choice(["deDE", "esES", "esMX",
                                                   "frFR", "koKR", "ruRU",
                                                   "zhCN", "zhTW"]),
              help=("If specified, use this locale to translate item names "
                    "(default is english)"))
def cli(host, port, user, password, locale):
    print host, port, user, password, locale


if __name__ == "__main__":
    cli(auto_envvar_prefix="EXPORT_AUCTIONS")
