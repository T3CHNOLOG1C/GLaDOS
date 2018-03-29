#!/usr/bin/env python3.6

import datetime

import discord
from discord.ext import commands

class Colors:
    """
    Color commands
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))
        
    @commands.command(pass_context=True)
    async def setcolor(self, ctx, color):
        """Choose your colored role."""
        user = ctx.message.author
        await ctx.message.delete()
        if color == "green":
            if self.bot.green_role in user.roles:
                await user.remove_roles(self.bot.green_role)
                await user.send("Color green removed.")
            else:
                await user.add_roles(self.bot.green_role)
                await user.send("Color green added.")
        elif color == "blue":
            if self.bot.blue_role in user.roles:
                await user.remove_roles(self.bot.blue_role)
                await user.send("Color blue removed.")
            else:
                await user.add_roles(self.bot.blue_role)
                await user.send("Color blue added.")
        elif color == "orange":
            if self.bot.orange_role in user.roles:
                await user.remove_roles(self.bot.orange_role)
                await user.send("Color orange removed.")
            else:
                await user.add_roles(self.bot.orange_role)
                await user.send("Color orange added.")
        elif color == "white":
            if self.bot.white_role in user.roles:
                await user.remove_roles(self.bot.white_role)
                await user.send("Color white removed.")
            else:
                await user.add_roles(self.bot.white_role)
                await user.send("Color white added.")
        elif color == "black":
            if self.bot.black_role in user.roles:
                await user.remove_roles(self.bot.black_role)
                await user.send("Color black removed.")
            else:
                await user.add_roles(self.bot.black_role)
                await user.send("Color black added.")
        elif color == "sand":
            if self.bot.sand_role in user.roles:
                await user.remove_roles(self.bot.sand_role)
                await user.send("Color sand removed.")
            else:
                await user.add_roles(self.bot.sand_role)
                await user.send("Color sand added.")
        elif color == "pink":
            if self.bot.pink_role in user.roles:
                await user.remove_roles(self.bot.pink_role)
                await user.send("Color pink removed.")
            else:
                await user.add_roles(self.bot.pink_role)
                await user.send("Color pink added.")
        else:
            await user.send("{} is not a togglable color.".format(color))

    @commands.command(pass_context=True)
    async def listcolors(self, ctx):
        """List available colors"""
        await ctx.send(":art: **__Colored roles:__**\n" + "- green\n- blue\n- orange\n- white\n- black\n- sand\n- pink")
        
    @commands.command(pass_context=True)
    async def colortest(self, ctx):
        """test cog"""
        await ctx.send("Color cog loaded and working :thumbsup:")


def setup(bot):
    bot.add_cog(Colors(bot))
