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
    async def color(self, ctx, str):
        """Choose your colored role."""
        user = ctx.message.author
        await ctx.message.delete()
        colors = [
            self.bot.green_role,
            self.bot.blue_role,
            self.bot.orange_role,
            self.bot.white_role,
            self.bot.black_role,
            self.bot.sand_role,
            self.bot.pink_role,
            self.bot.teal_role,
        ]
        applied_colors = []
        for color in colors:
            if color in user.roles:
                applied_colors.append(color)
        if str == "green":
            if not applied_colors:
                await user.add_roles(self.bot.green_role)
                await user.send("Color green added.")
            elif applied_colors[0] == self.bot.green_role:
                await user.remove_roles(self.bot.green_role)
                await user.send("Color green removed.")
            else:
                await user.send("You already have a color!")
        elif str == "blue":
            if not applied_colors:
                await user.add_roles(self.bot.blue_role)
                await user.send("Color blue added.")
            elif applied_colors[0] == self.bot.blue_role:
                await user.remove_roles(self.bot.blue_role)
                await user.send("Color blue removed.")
            else:
                await user.send("You already have a color!")
        elif str == "orange":
            if not applied_colors:
                await user.add_roles(self.bot.orange_role)
                await user.send("Color orange added.")
            elif applied_colors[0] == self.bot.orange_role:
                await user.remove_roles(self.bot.orange_role)
                await user.send("Color orange removed.")
            else:
                await user.send("You already have a color!")
        elif str == "white":
            if not applied_colors:
                await user.add_roles(self.bot.orange_role)
                await user.send("Color orange added.")
            elif applied_colors[0] == self.bot.white_role:
                await user.remove_roles(self.bot.white_role)
                await user.send("Color white removed.")
            else:
                await user.send("You already have a color!")
        elif str == "black":
            if not applied_colors:
                await user.add_roles(self.bot.black_role)
                await user.send("Color black added.")
            elif applied_colors[0] == self.bot.black_role:
                await user.remove_roles(self.bot.black_role)
                await user.send("Color black removed.")
            else:
                await user.send("You already have a color!")
        elif str == "sand":
            if not applied_colors:
                await user.add_roles(self.bot.sand_role)
                await user.send("Color sand added.")
            elif applied_colors[0] == self.bot.sand_role:
                await user.remove_roles(self.bot.sand_role)
                await user.send("Color sand removed.")
            else:
                await user.send("You already have a color!")
        elif str == "pink":
            if not applied_colors:
                await user.add_roles(self.bot.pink_role)
                await user.send("Color pink added.")
            elif applied_colors[0] == self.bot.pink_role:
                await user.remove_roles(self.bot.pink_role)
                await user.send("Color pink removed.")
            else:
                await user.send("You already have a color!")

        elif str == "teal":
            if not applied_colors:
                await user.add_roles(self.bot.teal_role)
                await user.send("Color Teal added.")
            elif applied_colors[0] == self.bot.teal_role:
                await user.remove_roles(self.bot.teal_role)
                await user.send("Color teal removed.")
            else:
                await user.send("You already have a color!")
        else:
            await user.send("`{}` is not an allowed color.".format(str))

    @commands.command(pass_context=True)
    async def listcolors(self, ctx):
        """List available colors"""
        await ctx.send(":art: **__Colored roles:__**\n" + "- green\n- blue\n- orange\n- white\n- black\n- sand\n- pink")

def setup(bot):
    bot.add_cog(Colors(bot))
