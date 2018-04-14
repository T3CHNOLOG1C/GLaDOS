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
                await user.send("Left MK8D role")

            else:
                await user.add_roles(self.bot.mk8d_role)
                await user.send("Joined MK8D role")

        elif role == "csgo":
            if self.bot.csgo_role in user.roles:
                await user.remove_roles(self.bot.csgo_role)
                await user.send("Left csgo role")

            else:
                await user.add_roles(self.bot.csgo_role)
                await user.send("Joined csgo role")

        elif role == "pubg":
            if self.bot.pubg_role in user.roles:
                await user.remove_roles(self.bot.pubg_role)
                await user.send("Left pubg role")

            else:
                await user.add_roles(self.bot.pubg_role)
                await user.send("Joined pubg role")

      
        else:
            await user.send("{} is not a togglable role".format(role))


def setup(bot):
    bot.add_cog(Toggle(bot))



    

