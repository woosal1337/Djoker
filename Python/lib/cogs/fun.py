import os
import sys
import asyncio
import discord
from random import choice, randint
from typing import Optional
import discord
from discord import Member, File
import requests
from discord.ext.commands import Cog
from discord.ext.commands import command

OWNERS = [792693374549360652]


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command(name="dark1337", aliases=["djokerdark", "dark"])
    async def dark_joke(self, ctx):
        djoke = requests.get("https://v2.jokeapi.dev/joke/dark").json()

        if (djoke["type"]) == "twopart":
            print(djoke["setup"] + "\n" + djoke["delivery"])
            return await ctx.send("- " + djoke["setup"] + "\n" + "- " + djoke["delivery"])

        print(djoke["joke"])
        return await ctx.send("- " + djoke["joke"])

    @command(name="programming1337", aliases=["djokerprogramming", "programming"])
    async def programming_joke(self, ctx):
        djoke = requests.get("https://v2.jokeapi.dev/joke/programming").json()

        if (djoke["type"]) == "twopart":
            print(djoke["setup"] + "\n" + djoke["delivery"])
            return await ctx.send("- " + djoke["setup"] + "\n" + "- " + djoke["delivery"])

        print(djoke["joke"])
        return await ctx.send("- " + djoke["joke"])

    @command(name="misc1337", aliases=["djokermisc", "misc"])
    async def misc_joke(self, ctx):
        djoke = requests.get("https://v2.jokeapi.dev/joke/misc").json()

        if (djoke["type"]) == "twopart":
            print(djoke["setup"] + "\n" + djoke["delivery"])
            return await ctx.send("- " + djoke["setup"] + "\n" + "- " + djoke["delivery"])

        print(djoke["joke"])
        return await ctx.send("- " + djoke["joke"])

    @command(name="pun1337", aliases=["djokerpun", "pun"])
    async def pun_joke(self, ctx):
        djoke = requests.get("https://v2.jokeapi.dev/joke/pun").json()

        if (djoke["type"]) == "twopart":
            print(djoke["setup"] + "\n" + djoke["delivery"])
            return await ctx.send("- " + djoke["setup"] + "\n" + "- " + djoke["delivery"])

        print(djoke["joke"])
        return await ctx.send("- " + djoke["joke"])

    @command(name="spooky1337", aliases=["djokerspooky", "spooky"])
    async def spooky_joke(self, ctx):
        djoke = requests.get("https://v2.jokeapi.dev/joke/spooky").json()

        if (djoke["type"]) == "twopart":
            print(djoke["setup"] + "\n" + djoke["delivery"])
            return await ctx.send("- " + djoke["setup"] + "\n" + "- " + djoke["delivery"])

        print(djoke["joke"])
        return await ctx.send("- " + djoke["joke"])

    @command(name="christmas1337", aliases=["djokerchristmas", "christmas"])
    async def christmas_joke(self, ctx):
        djoke = requests.get("https://v2.jokeapi.dev/joke/christmas").json()

        if (djoke["type"]) == "twopart":
            print(djoke["setup"] + "\n" + djoke["delivery"])
            return await ctx.send("- " + djoke["setup"] + "\n" + "- " + djoke["delivery"])

        print(djoke["joke"])
        return await ctx.send("- " + djoke["joke"])

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
