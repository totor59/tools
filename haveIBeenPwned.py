#!/usr/bin/python3
# coding: utf8

import urllib.request
from urllib.parse import quote
import click
import json


def header():
    title = "haveIBeenPwned"
    author = "t0t0r"
    click.secho("¦̵̱ ̵̱ ̵̱ ̵̱ ̵̱(̥̥ ͇̅└͇̅┘͇̅ (≡8כ−◦ "+title+" by "+author, bold=True,
                fg='magenta')
    print("")


@click.command(options_metavar='<options>')
@click.option('--breached', help='Getting all breaches for an account',
              metavar='<email>')
@click.option('--pasted', help='Getting all pastes for an account',
              metavar='<email>')
@click.option('--pwned', help='Check if a password is pwned or not',
              metavar='<password>')
def cli(breached, pasted, pwned):
    """A simple wrapper for haveibeenpwned.com API."""
    base_url = 'https://haveibeenpwned.com/api/v2/'
    if breached:
        url = base_url+'breachedaccount/'+quote(breached)
        resp = urllib.request.Request(url, headers={"User-Agent":"hibp-python"})
        try:
            handle = urllib.request.urlopen(resp).read().decode('utf-8')
            result = json.loads(handle)
            click.secho("OH NO — PWNED!\n", bold=True, fg="red")  
            for r in result:
                click.secho('Title:', bold=True)
                print(r['Title'])
                click.secho('Breach date:', bold=True)
                print(r['BreachDate'])
                click.secho('Description:', bold=True)
                print(r['Description'])
                click.secho('Compromised data:', bold=True)
                for i in r['DataClasses']:
                    print("   * "+i)
                click.secho('       ---------------         ', bold=True,
                            fg='red')
        except IOError as e:
            if e.code == 404:
            	click.secho("GOOD NEWS — NO PWNAGE FOUND!\n", fg='green',bold=True)
            else:
            	click.secho("Error "+str(e.code), err=True)
    elif pasted:
        url = base_url+'pasteaccount/'+quote(pasted)
        resp = urllib.request.Request(url, headers={"User-Agent":"hibp-python"})
        try:
            handle = urllib.request.urlopen(resp).read().decode('utf-8')
            result = json.loads(handle)
            click.secho("OH NO — PASTED!\n", bold=True, fg="red")  
            for r in result:
                click.secho('Website:', bold=True)
                print(r['Source'])
                click.secho('Id:', bold=True)
                print(r['Id'])
                if r['Title']:
                    click.secho('Title:', bold=True)
                    print(r['Title'])
                click.secho('Paste date:', bold=True)
                print(r['Date'])
                click.secho('Email count:', bold=True)
                print(r['EmailCount'])
                click.secho('       ---------------         ', bold=True,
                            fg='red')
        except IOError as e:
            if e.code == 404:
            	click.secho("GOOD NEWS — NO PASTE FOUND!\n", fg='green',bold=True)
            else:
            	click.secho("Error "+str(e.code), err=True)
    elif pwned:
        url = base_url+'pwnedpassword/'+quote(pwned)
        resp = urllib.request.Request(url, headers={"User-Agent":"hibp-python"})
        try:
            urllib.request.urlopen(resp)
            click.secho('PASSWORD FOUND CHANGE IT ASAP!', bold=True, fg="red")
        except urllib.error.HTTPError as e:
            click.secho('THIS PASSWORD SEEMS SAFE!', bold=True, fg="green")

if __name__ == '__main__':
    header()
    cli()

