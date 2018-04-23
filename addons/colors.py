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
        
        
    @commands.command(pass_context=True, aliases=['colour'])
    async def color(self, ctx, str=""):
        """Choose your colored role."""
        user = ctx.message.author
        await ctx.message.delete()
        lang = (ctx.invoked_with).capitalize()
        if not str:
            return await ctx.send("{} You forgot to choose a {}! You can see the full list with `.list{}`".format(user.mention, lang.lower(), lang.lower()), delete_after=10)
        
        str = str.lower()
        
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
        if applied_colors:
            cur_color = applied_colors[0]
        if str == "green":
            if not applied_colors:
                await user.add_roles(self.bot.green_role)
                await ctx.send("{} {} green added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.green_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.green_role)
                await ctx.send("{} {} green added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.green_role)
                await ctx.send("{} {} green removed.".format(user.mention, lang), delete_after=5)
        elif str == "blue":
            if not applied_colors:
                await user.add_roles(self.bot.blue_role)
                await ctx.send("{} {} blue added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.blue_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.blue_role)
                await ctx.send("{} {} blue added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.blue_role)
                await ctx.send("{} {} blue removed.".format(user.mention, lang), delete_after=5)
        elif str == "orange":
            if not applied_colors:
                await user.add_roles(self.bot.orange_role)
                await ctx.send("{} {} orange added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.orange_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.orange_role)
                await ctx.send("{} {} orange added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.orange_role)
                await ctx.send("{} {} orange removed.".format(user.mention, lang), delete_after=5)
        elif str == "white":
            if not applied_colors:
                await user.add_roles(self.bot.white_role)
                await ctx.send("{} {} white added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.white_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.white_role)
                await ctx.send("{} {} white added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.white_role)
                await ctx.send("{} {} white removed.".format(user.mention, lang), delete_after=5)
        elif str == "black":
            if not applied_colors:
                await user.add_roles(self.bot.black_role)
                await ctx.send("{} {} black added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.black_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.black_role)
                await ctx.send("{} {} black added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.black_role)
                await ctx.send("{} {} black removed.".format(user.mention, lang), delete_after=5)
        elif str == "sand":
            if not applied_colors:
                await user.add_roles(self.bot.sand_role)
                await ctx.send("{} {} sand added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.sand_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.sand_role)
                await ctx.send("{} {} sand added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.sand_role)
                await ctx.send("{} {} sand removed.".format(user.mention, lang), delete_after=5)
        elif str == "pink":
            if not applied_colors:
                await user.add_roles(self.bot.pink_role)
                await ctx.send("{} {} pink added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.pink_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.pink_role)
                await ctx.send("{} {} pink added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.pink_role)
                await ctx.send("{} {} pink removed.".format(user.mention, lang), delete_after=5)
        elif str == "teal":
            if not applied_colors:
                await user.add_roles(self.bot.teal_role)
                await ctx.send("{} {} teal added.".format(user.mention, lang), delete_after=5)
            elif cur_color != self.bot.teal_role:
                await user.remove_roles(cur_color)
                await ctx.send("{} {} {} removed.".format(user.mention, lang, cur_color.name.lower()), delete_after=5)
                await user.add_roles(self.bot.teal_role)
                await ctx.send("{} {} teal added.".format(user.mention, lang), delete_after=5)
            else:
                await user.remove_roles(self.bot.teal_role)
                await ctx.send("{} {} teal removed.".format(user.mention, lang), delete_after=5)
        else:
            await ctx.send("{} `{}` is not a permissible {}.".format(user.mention, str, lang), delete_after=5)

    @commands.command(pass_context=True, aliases=['listcolours', 'listcolor', 'listcolour'])
    async def listcolors(self, ctx):
        """List available colors"""
        if ctx.invoked_with == "listcolor" or ctx.invoked_with == "listcolors":
            lang = "Color"
        else:
            lang = "Colour"
        await ctx.send(":art: **__{}ed roles:__**\n- green\n- blue\n- orange\n- white\n- black\n- sand\n- pink\n- teal".format(lang))

def setup(bot):
    bot.add_cog(Colors(bot))
