#! /usr/bin/python
import server
from .. import minecraft

""" hello world test app

    @author: goldfish"""

mc = minecraft.Minecraft.create(server.address)
mc.postToChat("Hello, Minecraft!")
