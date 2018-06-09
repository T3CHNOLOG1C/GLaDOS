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
    async def togglerole(self, ctx, role):
        """toggle some hidden roles"""
        
        user = ctx.message.author
        await ctx.message.delete()


        if role == "MK8D":
            if self.bot.mk8d_role in user.roles:
                await user.remove_roles(self.bot.mk8d_role)
                msg = "Left MK8D role"
                await user.send(msg)

            else:
                await user.add_roles(self.bot.mk8d_role)
                msg = "Joined MK8D role"
                await user.send(msg)

        elif role == "csgo":
            if self.bot.csgo_role in user.roles:
                await user.remove_roles(self.bot.csgo_role)
                msg = "Left csgo role"
                await user.send(msg)

            else:
                await user.add_roles(self.bot.csgo_role)
                msg = "Joined csgo role"
                await user.send(msg)

        elif role == "pubg":
            if self.bot.pubg_role in user.roles:
                await user.remove_roles(self.bot.pubg_role)
                msg = "Left PUBG role"
                await user.send(msg)

            else:
                await user.add_roles(self.bot.pubg_role)
                msg = "Joined PUBG role"
                await user.send(msg)

        elif role == "cah":
            if self.bot.cah_role in user.roles:
                await user.remove_roles(self.bot.cah_role)
                msg = "Left CAH role"
                await user.send(msg)

            else:
                await user.add_roles(self.bot.cah_role)
                msg = "Joined CAH role"
                await user.send(msg)

        elif role == "spla2n":
            if self.bot.spla2n_role in user.roles:
                await user.remove_roles(self.bot.spla2n_role)
                msg = "Left Splatoon 2 role"
                await user.send(msg)

            else:
                await user.add_roles(self.bot.spla2n_role)
                msg = "Joined Splatoon 2 role"
                await user.send(msg)
      
        elif role == "redeclipse":
            if self.bot.redeclipse_role in user.roles:
                await user.remove_roles(self.bot.redeclipse_role)
                msg = "Left Red Eclipse role"
                await user.send(msg)

            else:
                await user.add_roles(self.bot.redeclipse_role)
                msg = "Joined Red Eclipse role"
                await user.send(msg)
      
        else:
            msg = "{} is not a togglable role".format(role)
            await user.send(msg)

def setup(bot):
    bot.add_cog(Toggle(bot))



    

