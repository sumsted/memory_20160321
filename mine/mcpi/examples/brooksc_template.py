#!/usr/bin/env python

#import the minecraft.py module from the minecraft directory
import server
from .. import minecraft


def main():
    mc = minecraft.Minecraft.create(server.address)
    # write the rest of your code here...
    mc.postToChat("Hello MCPIPY World!")


if __name__ == "__main__":
    main()
