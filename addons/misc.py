from datetime import datetime

from discord import Embed, errors, Color, Member
from discord.ext import commands


class Misc(commands.Cog):
    """
    Miscellaneous commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong!"""
        mtime = ctx.message.created_at
        currtime = datetime.now()
        latency = currtime - mtime
        ptime = str(latency.microseconds / 1000.0)
        await ctx.send(":ping_pong:! Pong! Response time: {} ms".format(ptime))
        return

    @commands.command(pass_context=True, aliases=['mc'])
    async def membercount(self, ctx):
        """Prints current member count"""
        await ctx.send("{} currently has {} members!"
                       "".format(ctx.guild.name, len(ctx.guild.members)))
        return

    @commands.command()
    async def about(self, ctx):
        """About GLaDOS."""
        await ctx.send("View my source code here: https://github.com/T3CHNOLOG1C/GLaDOS")

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clear(self, ctx, amount):
        """Clears a given amount of messages. (Mods only)"""

        channel = ctx.message.channel
        try:
            n = int(amount) + 1
        except ValueError:
            return await ctx.send("Please mention a valid amount of messages!")

        try:
            await channel.purge(limit=n)
            await ctx.send("🗑️ Cleared {} messages in this channel!".format(amount))
            try:
                emb = Embed(title="Messages Cleared", colour=Color.red())
                emb.add_field(
                    name="Mod:", value=ctx.message.author, inline=True)
                emb.add_field(name="Channel:",
                              value=ctx.message.channel, inline=True)
                emb.add_field(name="Amount:", value=amount, inline=True)
                logchannel = self.bot.logs_channel
                await logchannel.send("", embed=emb)
            except errors.Forbidden:
                await ctx.send("💢 I dont have permission to do this.")

        except errors.Forbidden:
            await ctx.say("💢 I don't have permission to do this.")

    @commands.command()
    async def userinfo(self, ctx):
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            member = ctx.message.author
        uname = member.name
        discrim = member.discriminator
        Uid = member.id
        displayName = member.display_name
        isBot = member.bot
        cTime = member.created_at
        jTime = member.joined_at
        str1 = "{}#{}".format(uname, discrim)
        str2 = "{}".format(Uid)
        if displayName == uname:
            displayName = "None"
        str3 = "{}".format(displayName)
        str4 = "{}".format(str(isBot))
        str5 = "{}".format(cTime)
        str6 = "{}".format(jTime)
        emb = Embed(title="Userinfo", color=0x00ff00)
        emb.add_field(name="Member", value=str1 + "\n", inline=True)
        emb.add_field(name="ID", value=str2 + "\n", inline=True)
        emb.add_field(name="Nickname", value=str3 + "\n", inline=True)
        emb.add_field(name="Bot?", value=str4 + "\n", inline=True)
        emb.add_field(name="Account Created", value=str5 + "\n", inline=True)
        emb.add_field(name="Joined Server", value=str6 + "\n", inline=True)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send("", embed=emb)

    @commands.command()
    async def bean(self, ctx, member: Member=None, *, reason: str=""):
        """Ban a member. (Staff Only)"""
        if not member:
            await ctx.send("Please mention a user.")
            return
        if member == ctx.message.author:
            await ctx.send("You cannot ban yourself!")
            return
        elif ctx.me is member:
            await ctx.send("I am unable to ban myself to prevent stupid mistakes.\n"
                           "Please ban me by hand!")
            return
        else:
            await ctx.send("I've banned {}. <a:abeanhammer:511352809245900810>".format(member))

    @commands.command()
    async def kicc(self, ctx, member: Member=None, *, reason: str=""):
        """Kick a member. (Staff Only)"""
        if not member:
            await ctx.send("Please mention a user.")
            return
        elif member is ctx.message.author:
            await ctx.send("You cannot kick yourself!")
            return
        elif ctx.me is member:
            await ctx.send("I am unable to kick myself to prevent stupid mistakes.\n"
                           "Please kick me by hand!")
            return
        await ctx.send("I've kicked {}.".format(member))

    @commands.command()
    async def moot(self, ctx, member: Member, *, reason=""):
        """Mutes a user. (Staff Only)"""

        if member is ctx.message.author:
            await ctx.send("You cannot mute yourself!")
            return
        elif ctx.me is member:
            await ctx.send("I can not mute myself!")
            return
        await ctx.send("{} can no longer speak!".format(member))

    @commands.command()
    async def unmoot(self, ctx, member: Member, *, reason=""):
        """Unmutes a user. (Staff Only)"""

        await ctx.send("{} is no longer muted!".format(member))

    @commands.command()
    async def warm(self, ctx, member: Member, *, reason=""):
        """
        Warn members. (Staff Only)
        - First warn : nothing happens, a simple warning
        - Second warn : muted until an the admin who issued the warning decides to unmute the user.
        - Third warn : kicked
        - Fourth warn : kicked
        - Fifth warn : banned
        """

        if member is ctx.message.author:
            await ctx.send("You cannot warn yourself!")
            return
        elif ctx.me is member:
            await ctx.send("I can not warn myself!")
            return
        await ctx.send("🚩 I've warned {}.".format(member))

def setup(bot):
    bot.add_cog(Misc(bot))
