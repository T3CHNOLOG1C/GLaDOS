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
        colors = [
            self.bot.green_role,
            self.bot.blue_role,
            self.bot.orange_role,
            self.bot.white_role,
            self.bot.black_role,
            self.bot.sand_role,
            self.bot.pink_role,
        ]
        
    @commands.command(pass_context=True)
    async def color(self, ctx, color):
        """Choose your colored role."""
        user = ctx.message.author
        await ctx.message.delete()
        applied_colors = []
        for color in colors:
            if color in user.roles:
                applied_colors.append(color)
        if len(applied_colors) > 1:
            return await user.send("You already have a color!")
        if color == "green":
            if not applied_colors:
                await user.add_roles(self.bot.green_role)
                await user.send("Color green added.")
            else:
                await user.remove_roles(self.bot.green_role)
                await user.send("Color green removed.")
        elif color == "blue":
            if not applied_colors:
                await user.add_roles(self.bot.blue_role)
                await user.send("Color blue added.")
            else:
                await user.remove_roles(self.bot.blue_role)
                await user.send("Color blue removed.")
        elif color == "orange":
            if not applied_colors:
                await user.add_roles(self.bot.orange_role)
                await user.send("Color orange added.")
            else:
                await user.remove_roles(self.bot.orange_role)
                await user.send("Color orange removed.")
        elif color == "white":
            if not applied_colors:
                await user.add_roles(self.bot.orange_role)
                await user.send("Color orange added.")
            else:
                await user.remove_roles(self.bot.orange_role)
                await user.send("Color orange removed.")
        elif color == "black":
            if not applied_colors:
                await user.add_roles(self.bot.black_role)
                await user.send("Color black added.")
            else:
                await user.remove_roles(self.bot.black_role)
                await user.send("Color black removed.")
        elif color == "sand":
            if not applied_colors:
                await user.add_roles(self.bot.sand_role)
                await user.send("Color sand added.")
            else:
                await user.remove_roles(self.bot.sand_role)
                await user.send("Color sand removed.")
        elif color == "pink":
            if not applied_colors:
                await user.add_roles(self.bot.pink_role)
                await user.send("Color pink added.")
            else:
                await user.remove_roles(self.bot.pink_role)
                await user.send("Color pink removed.")
        else:
            await user.send("{} is not a togglable color.".format(color))

    @commands.command(pass_context=True)
    async def listcolors(self, ctx):
        """List available colors"""
        await ctx.send(":art: **__Colored roles:__**\n" + "- green\n- blue\n- orange\n- white\n- black\n- sand\n- pink")

def setup(bot):
    bot.add_cog(Colors(bot))
