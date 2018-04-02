#!/usr/bin/env python3.6

import datetime

import discord
from discord.ext import commands

class Misc:
    """
    Miscellaneous commands
    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))
        
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong!"""
        mtime = ctx.message.created_at
        currtime = datetime.datetime.now()
        latency = currtime - mtime
        ptime = str(latency.microseconds / 1000.0)
        return await ctx.send(":ping_pong:! Pong! Response time: {} ms".format(ptime))

    @commands.command(pass_context=True, aliases=['mc'])
    async def membercount(self, ctx):
        """Prints current member count"""
        return await ctx.send("{} currently has {} members!".format(self.bot.guild.name, self.bot.guild.members))
    
    @commands.command()
    async def about(self, ctx):
        """About GLaDOS."""
        return await ctx.send("View my source code here: https://github.com/T3CHNOLOG1C/GLaDOS")
        
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
        except discord.errors.Forbidden:
            await ctx.say("💢 I don't have permission to do this.")

    @commands.command()
    async def userinfo(self, ctx, member):
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            await ctx.send("Please mention a user.")
            return
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
        emb = discord.Embed(title="Userinfo", color= 0x00ff00)
        emb.add_field(name="Member", value=str1 + "\n", inline=True)
        emb.add_field(name="ID", value=str2 + "\n", inline=True)
        emb.add_field(name="Nickname", value=str3 + "\n", inline=True)
        emb.add_field(name="Bot?", value=str4 + "\n", inline=True)
        emb.add_field(name="Account Created", value=str5 + "\n", inline=True)
        emb.add_field(name="Joined Server", value=str6 + "\n", inline=True)
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send("", embed=emb)
            
def setup(bot):
    bot.add_cog(Misc(bot))
