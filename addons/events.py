from discord import Embed, Colour, utils
from discord.ext import commands

class Events(commands.Cog):
    """
    bot events
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        user = member
        emb = Embed(title="Member Joined", colour=Colour.green())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.memberlogs_channel
        await logchannel.send("", embed=emb)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        user = member
        emb = Embed(title="Member Left", colour=Colour.green())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.memberlogs_channel
        await logchannel.send("", embed=emb)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        user = member
        emb = Embed(title="Member Unbanned", colour=Colour.red())
        emb.add_field(name="Member:", value=member.name, inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message
        emote = utils.get(self.bot.guild.emojis, name='okretard')
        if msg.author.id in [243019821564952578, 208370244207509504, 286488483994927109, 334191144118386698, 102743440026009600]: # <3
            await msg.add_reaction(emote)
        else:
            pass


def setup(bot):
    bot.add_cog(Events(bot))
