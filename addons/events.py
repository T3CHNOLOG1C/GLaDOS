#!/usr/bin/env python3
import time
import discord
from discord.ext import commands

class Events:
    """
    bot events
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))
        
    async def on_member_join(self, member):
        user = member
        geturl = await self.bot.get_user_info(user)
        emb = discord.Embed(title="Member Joined", colour=discord.Colour.green())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.memberlogs_channel
        await logchannel.send("", embed=emb)

def setup(bot):
    bot.add_cog(Events(bot))
