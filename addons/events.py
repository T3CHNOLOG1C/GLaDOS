#!/usr/bin/env python3
from discord import Embed, Colour


class Events:
    """
    bot events
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))

    async def on_member_join(self, member):
        user = member
        emb = Embed(title="Member Joined", colour=Colour.green())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.memberlogs_channel
        await logchannel.send("", embed=emb)

    async def on_member_remove(self, member):
        user = member
        emb = Embed(title="Member Left", colour=Colour.green())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.memberlogs_channel
        await logchannel.send("", embed=emb)

    async def on_member_unban(self, guild, member):
        user = member
        emb = Embed(title="Member Unbanned", colour=Colour.red())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)


def setup(bot):
    bot.add_cog(Events(bot))

