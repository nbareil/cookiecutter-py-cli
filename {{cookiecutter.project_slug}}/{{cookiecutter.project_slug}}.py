#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import click


@click.group()
def cli(dir):
    pass


@click.command()
def new():
    pass


cli.add_command(new)

if __name__ == "__main__":
    cli()
