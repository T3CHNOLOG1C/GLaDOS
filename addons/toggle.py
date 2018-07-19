import datetime

import discord
from discord.ext import commands


class Toggle:
    """
    Toggle channel and role cmds (not colors)

    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded".format(self.__class__.__name__))


    @commands.command(pass_context=True)
    async def togglechannel(self, ctx, channel):
        """Toggle access to some hidden channels"""

        user = ctx.message.author
        await ctx.message.delete()

        if channel == "nsfw":

            if self.bot.nsfw_role in user.roles:
                await user.remove_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels revoked.")
            else:
                await user.add_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels granted.")
        else:
            await user.send("{} is not a togglable channel.".format(channel))

    @commands.command(pass_context=True)
    async def togglerole(self, ctx, role=""):
        """toggle some hidden roles"""
        
        user = ctx.message.author
        
        if role == "":
            embed = discord.Embed(title="Toggleable Roles:", color=discord.Color.dark_teal())
            embed.description = """
- :race_car: Mario Kart 8 Deluxe: MK8D
- :squid: Splatoon 2: spla2n
- :card_box: Cards Against Humanity: cah
- :bomb: Counter-Strike: Global Offensive: csgo
- :gun: PUBG: pubg
- :red_circle: Red Eclipse: redeclipse
- :robot: Titanfall (2): titanfall
- :boxing_glove: Super Smash Bros.: smash
- :shopping_cart: Fortnite: fortnite
"""
            await ctx.send("", embed=embed)


        elif role == "MK8D":
            if self.bot.mk8d_role in user.roles:
                await user.remove_roles(self.bot.mk8d_role)
                msg = "Left MK8D role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.mk8d_role)
                msg = "Joined MK8D role"
                await ctx.send(msg)

        elif role == "csgo":
            if self.bot.csgo_role in user.roles:
                await user.remove_roles(self.bot.csgo_role)
                msg = "Left csgo role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.csgo_role)
                msg = "Joined csgo role"
                await ctx.send(msg)

        elif role == "pubg":
            if self.bot.pubg_role in user.roles:
                await user.remove_roles(self.bot.pubg_role)
                msg = "Left PUBG role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.pubg_role)
                msg = "Joined PUBG role"
                await ctx.send(msg)

        elif role == "cah":
            if self.bot.cah_role in user.roles:
                await user.remove_roles(self.bot.cah_role)
                msg = "Left CAH role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.cah_role)
                msg = "Joined CAH role"
                await ctx.send(msg)

        elif role == "spla2n":
            if self.bot.spla2n_role in user.roles:
                await user.remove_roles(self.bot.spla2n_role)
                msg = "Left Splatoon 2 role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.spla2n_role)
                msg = "Joined Splatoon 2 role"
                await ctx.send(msg)
      
        elif role == "redeclipse":
            if self.bot.redeclipse_role in user.roles:
                await user.remove_roles(self.bot.redeclipse_role)
                msg = "Left Red Eclipse role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.redeclipse_role)
                msg = "Joined Red Eclipse role"
                await ctx.send(msg)
                
        elif role == "titanfall":
            if self.bot.titanfall_role in user.roles:
                await user.remove_roles(self.bot.titanfall_role)
                msg = "Left Titanfall role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.titanfall_role)
                msg = "Joined Titanfall role"
                await ctx.send(msg)
      
        elif role == "smash":
            if self.bot.smashbros_role in user.roles:
                await user.remove_roles(self.bot.smashbros_role)
                msg = "Left Smash Bros role"
                await ctx.send(msg)

            else:
                await user.add_roles(self.bot.smashbros_role)
                msg = "Joined Smash Bros role"
                await ctx.send(msg)
      
        elif role == "fortnite":
            if self.bot.fortnite_role in user.roles:
                await user.remove_roles(self.bot.fortnite_role)
                msg = "Left Fortnite role"
                await ctx.send(msg)
                
            else:
                await user.add_roles(self.bot.fortnite_role)
                msg = "Joined Fortnite role"
                await ctx.send(msg)
        else:
            msg = "{} is not a togglable role".format(role)
            await ctx.send(msg)

def setup(bot):
    bot.add_cog(Toggle(bot))



    

