from datetime import datetime

from discord import *
from discord.ext import commands
from typing import Union


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
            except Forbidden:
                await ctx.send("💢 I dont have permission to do this.")

        except Forbidden:
            await ctx.say("💢 I don't have permission to do this.")

    @commands.command(aliases=['ui', 'onion'])
    async def userinfo(self, ctx, member: Union[Member, int, str] = None):
        """Prints userinfo on a member"""
        inserver = None
        if member == None:
            user = ctx.author
            inserver  = True
        elif isinstance(member, int):
            try:
                user = await self.bot.fetch_user(member)
                inserver = False
            except NotFound:
                await ctx.send("💢 I cannot find that user")
        elif isinstance(member, Member):
            user = member
            inserver = True
        elif isinstance(member, str):
            await ctx.send("💢 I cannot find that user")
            return  

        if inserver:
            embed = Embed(title=f'**Userinfo for {user.name}#{str(user.discriminator)}**', color=user.color.value)
            embed.description = f"""**User's ID:** {str(user.id)} \n **Join date:** {str(user.joined_at)} \n**Created on** {str(user.created_at)}\n **Current Status:** {str(user.status).upper() if str(user.status).lower() == "dnd" else str(user.status).title()}\n **User Activity:**: {str(user.activity)} \n **Default Profile Picture:** {str(user.default_avatar).title()}\n **Current Display Name:** {user.display_name}\n**Nitro Boost Date:** {str(user.premium_since)}\n **Current Top Role:** {str(user.top_role)}\n **Bot** {user.bot}\n **Color:** {str(hex(user.color.value)[2:])}"""
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)

        elif not inserver:
            try:
                ban = await ctx.guild.fetch_ban(user)
            except NotFound:
                ban = None

            embed = Embed(title=f'**Userinfo for {user.name}#{str(user.discriminator)}**')
            embed.description = f"**User's ID:** {str(user.id)} \n **Default Profile Picture:** {str(user.default_avatar)} \n  **Created on:** {str(user.created_at)}\n **Bot:** {user.bot}\n {f'**Banned, reason:** {ban.reason}'if ban is not None else ''}"
            embed.set_footer(text=f'{user.name}#{user.discriminator} is not in your server.')
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['avi'])
    async def avatar(self, ctx, member: Union[Member, int, str] = None):
        """Gets a user's avatar"""
        # TODO move this code to its own function
        inserver = None
        if member is None:
            user = ctx.author
            inserver  = True
        elif isinstance(member, int):
            try:
                user = await self.bot.fetch_user(member)
                inserver = False
            except NotFound:
                await ctx.send("💢 I cannot find that user")
        elif isinstance(member, Member):
            user = member
            inserver = True
        elif isinstance(member, str):
            await ctx.send("💢 I cannot find that user")
            return
        
        embed = Embed(title= f"Avatar for {user.name}#{user.discriminator}", color=user.color.value if inserver else 0x99aab5)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def bean(self, ctx, member: Member=None, *, reason: str=""):
        """Beans a member."""

        await ctx.send("I've beaned {}. <a:abeanhammer:511352809245900810>".format(member))

    @commands.command()
    async def kicc(self, ctx, member: Member=None, *, reason: str=""):
        """Kicc a member. """
       
        await ctx.send("I've kicced {}.".format(member))

    @commands.command()
    async def moot(self, ctx, member: Member, *, reason=""):
        """Moots a user. """

        await ctx.send("{} can no longer speak!".format(member))

    @commands.command()
    async def unmoot(self, ctx, member: Member, *, reason=""):
        """unmoots a user."""

        await ctx.send("{} is no longer mooted!".format(member))

    @commands.command()
    async def warm(self, ctx, member: Member, *, reason=""):
        """
        Woah, toasty!
        """
        await ctx.send("🚩 I've warmed {}.".format(member))

def setup(bot):
    bot.add_cog(Misc(bot))
