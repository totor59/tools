#!/usr/bin/python3
#coding: utf8

import urllib.request
from urllib.parse import quote
import click
import sys

def header():
    title = "getMacVendor"
    author = "t0t0r"
    click.secho("¦̵̱ ̵̱ ̵̱ ̵̱ ̵̱(̥̥ ͇̅└͇̅┘͇̅ (≡8כ−◦ "+title+" by "+author, bold=True, fg='magenta')
    print("")



def get_mac_vendor(mac_addr):
    url = "http://api.macvendors.com/"+quote(mac_addr)
    resp = urllib.request.Request(url)
    try:
        handle = urllib.request.urlopen(url)
        click.secho(" !Vendor: "+handle.read().decode("utf-8"), fg='green', bold=True)
    except IOError as e:
        if e.code == 404:
            click.secho(" !Vendor not found", fg='red',bold=True)
        else:
            click.secho("Error "+e.code, fg='red', bold=True)
    

if __name__ == "__main__":
    header()
    try:
        mac_addr = sys.argv[1]
    except IndexError:
        print("Usage: MACvendor.py <mac_addr>")
        print("Ex: python MACvendor.py 00:00:00:00:00:00")
        sys.exit(1)
    get_mac_vendor(mac_addr)
