# WotLK Auctions Dump

A commandline utility to export WoW auction house data to JSON.

## Motivation

The auction house simulates a market with real supply and demand mechanisms, because it is entirely driven by real people. Analyzing the current supply to be able to make informed decisions about when to buy and when to sell is an appealing task, but it needs data. The exported data from this script can be used to feed custom clients that help with this.

## Requirements

    Python 2.7 or higher

## Installation on Windows

    virtualenv venv
    venv/Scripts/activate.bat
    pip install peewee

## Build on Windows

    pyinstaller export_auctions.py
    dist/export_auctions.exe

## Usage

export\_auctions --user="readonly_user" --password="\*\*\*\*\*" --locale="deDE" --outfile="auctions.json"