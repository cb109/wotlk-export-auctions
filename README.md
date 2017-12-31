# WotLK Auctions Dump

A commandline utility to export WoW auction house data to JSON.

The idea is to make the information visible in the auction house available for external clients.

## Motivation

The auction house simulates a market with real supply-and-demand mechanisms, because it is entirely driven by real people. Analyzing the current supply to be able to make informed decisions about when to buy and when to sell is an appealing task, but it needs data: The exported data from this script can be used to feed custom clients that help with this.

## Requirements

- [Python 2.7 x64](https://www.python.org/downloads/release/python-2714/)
- A local or remote [TrinityCore](https://github.com/TrinityCore/TrinityCore) Server (tested against a Windows 7 x64 build from branch **3.3.5**)

## Installation on Windows

First clone the project and open a `cmd.exe`. Make sure to `cd` into the project directory, then:

    > virtualenv venv
    > venv/Scripts/activate.bat
    > python -m pip install --upgrade pip
    > pip install -r requirements.txt

## Build on Windows

The script and all its dependencies can be built into a single executable for easy deployment.

    > pyinstaller exportauctions.py --onefile
    # Result is placed in: dist/exportauctions.exe

## Usage

    # See usage info
    > python exportauctions.py --help

    # Output results to STDOUT
    > python exportauctions.py --user myuser --password mypassword

    # Output results to a file and use a specific locale
    > python exportauctions.py --user myuser --password mypassword --locale deDE --outfile auctions.json


## Example Result

```
{
    "locale": "deDE",
    "auctions": [
        {
            "buyoutprice": 50500,
            "item": {
                "count": 20,
                "name": "Morning Glory Dew",
                "requiredlevel": 45,
                "quality": 1,
                "id": 8766,
                "locale_name": "Trichterwindentau"
            },
            "houseid": 6,
            "deposit": 2400,
            "time": 1514799636,
            "owner": {
                "name": "Buyer"
            },
            "id": 6,
            "lastbid": 0,
            "startbid": 5000
        },
        {
            "buyoutprice": 10100,
            "item": {
                "count": 5,
                "name": "Crusty Flatbread",
                "requiredlevel": 65,
                "quality": 1,
                "id": 33449,
                "locale_name": "Knuspriges Fladenbrot"
            },
            "houseid": 18,
            "deposit": 1260,
            "time": 1514910251,
            "owner": {
                "name": "Testboy"
            },
            "id": 18,
            "lastbid": 0,
            "startbid": 3187
        }
    ],
    "time": 1514744535337.0
}
```