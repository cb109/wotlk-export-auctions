# WotLK Auctions Dump

A commandline utility to export WoW auction house data to JSON.

## Motivation

The auction house simulates a market with real supply-and-demand mechanisms, because it is entirely driven by real people. Analyzing the current supply to be able to make informed decisions about when to buy and when to sell is an appealing task, but it needs data: The exported data from this script can be used to feed custom clients that help with this.

## Requirements

- [Python 2.7 x64](https://www.python.org/downloads/release/python-2714/)
- A local or remote [TrinityCore](https://github.com/TrinityCore/TrinityCore) Server (tested against a Windows 7 x64 build from branch **3.3.5**)

## Installation on Windows

First clone the project and open a `cmd.exe`. Make sure to `cd` into the project directory, then:

    > virtualenv venv
    > venv/Scripts/activate.bat
    > pip install -r requirements.txt

## Build on Windows

The script and all its dependencies can be built into a single executable for easy deployment.

    > pyinstaller export_auctions.py --onefile
    # Result is placed in: dist/export_auctions.exe

## Usage Examples

    # See usage info
    > python exportauctions.py --help

    # Output results to STDOUT
    > python exportauctions.py -u readonly_user -P mypassword

    # Output results to a file and use a specific locale
    > python exportauctions.py -u readonly_user -P mypassword --locale deDE --outfile auctions.json