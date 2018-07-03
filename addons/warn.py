import asyncio
import json
import time
from os import execv
from sys import argv
from subprocess import call

import discord
from discord.ext import commands


class Warn:
    """
    Warn commands
    """
    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))

    async def dm(self, member, message):
        """DM the user and catch an eventual exception."""
        try:
            await member.send(message)
        except:
            pass

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def warn(self, ctx, member, *, reason=""):
        """
        Warn members. (Staff Only)
        A user ID can be used instead of mentionning the user.
        - First warn : nothing happens, a simple warning
        - Second warn : muted until an the admin who issued the warning decides to unmute the user.
        - Third warn : kicked
        - Fourth warn : kicked
        - Fifth warn : banned
        """
        author = ctx.message.author
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")
        if member == ctx.message.author:
            return await ctx.send("You cannot warn yourself!")
        if self.bot.staff_role in member.roles and not self.bot.owner_role in author.roles:
            return await ctx.send("You cannot warn other staff members!")
        elif self.bot.owner_role in member.roles:
            return await ctx.send("💢 I don't have the permission to do that!")
        
        with open("database/warns.json", "r") as f:
            js = json.load(f) # https://hastebin.com/ejizaxasav.scala
        
        id = str(member.id)
        if id not in js:
            amount_of_warns = 1
            js[id] = {"warns": []}
        else:
            amount_of_warns = len(js[id]["warns"]) + 1

        member_name = "{}#{}".format(member.name, member.discriminator)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        author_name = "{}#{}".format(author.name, author.discriminator)

        js[id]["amount"] = amount_of_warns
        js[id]["warns"].append({
            "name": member_name,
            "timestamp": timestamp,
            "reason": reason,
            "author": author_name,
            "author_id": author.id,
        })
        await ctx.send("🚩 I've warned {}. The user now has {} warns.".format(member, amount_of_warns))
        if reason == "":
            await self.dm(member, "You have been warned in {}.".format(ctx.guild.name))
        else:
            await self.dm(member, "You have been warned in {} for the following reason :\n{}\n".format(ctx.guild.name, reason))
        emb = discord.Embed(title="Member Warned", colour=discord.Colour.orange())
        emb.add_field(name="Member:", value=member, inline=True)
        emb.add_field(name="Warning Number:", value=amount_of_warns, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
        if reason == "":
            reason = "No reason specified."
        emb.add_field(name="Reason:", value=reason, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)

        if amount_of_warns == 1:
            await self.dm(member, "This is your first warning. The next warning will automatically mute you.")
        elif amount_of_warns == 2:
            await self.dm(member, "This is your second warning, so you've been muted. You will be unmuted whenever the admin who warned you decides to unmute you.\nYou will be DM'ed when a mod unmutes you.\n**Do not ask mods to unmute you, as doing so might extend the duration of the mute**")
            await self.dm(member, "Your next warn will result in being kicked from the server.")
            await member.add_roles(self.bot.muted_role)
        elif amount_of_warns == 3:
            await self.dm(member, "This is your third warning, so you have been kicked. Please note that **the next warn will result in another kick!**")
            await member.kick(reason="Third warn")
        elif amount_of_warns == 4:
            await self.dm(member, "You have been kicked from the server. This is your fourth and final warning. **__The next warning will result in an automatic permanent ban.__**")
            await member.kick(reason="Fourth warn")
        elif amount_of_warns >= 5:
            await self.dm(member, "You have reached your fifth warning. You are now permanently banned from this server.")
            await member.ban(delete_message_days=0, reason="Fifth warn.")

        with open("database/warns.json", "w") as f:
            json.dump(js, f, indent=2, separators=(',', ':'))

    @commands.command()
    async def listwarns(self, ctx):
        """
        List your own warns or someone else's warns.
        Only the staff can view someone else's warns
        """

        try:
            member = ctx.message.mentions[0]
            if self.bot.staff_role in ctx.message.author.roles:
                has_perms = True
            else:
                has_perms = False
        except IndexError:
            member = ctx.message.author
            has_perms = True
        if not has_perms:
            return await ctx.send("{} You don't have permission to list other member's warns!".format(ctx.message.author.mention))

        with open("database/warns.json", "r") as f:
            js = json.load(f)
        
        id = str(member.id)
        if id not in js:
            return await ctx.send("No warns found!")
        embed = discord.Embed(color=member.colour)
        embed.set_author(name="List of warns for {} :".format(member), icon_url=member.avatar_url)

        for nbr, warn in enumerate(js[id]["warns"]):
            content = "{}".format(warn["reason"])
            author = await self.bot.get_user_info(warn["author_id"])
            content += "\n*Warn author : {} ({})*".format(warn["author"], author.mention)
            embed.add_field(name="\n\n#{}: {}".format(nbr + 1, warn["timestamp"]), value=content, inline=False)
        
        await ctx.send("", embed=embed)

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def clearwarns(self, ctx, member):
        """Clear all of someone's warns. (Staff only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")

        with open("database/warns.json", "r") as f:
            js = json.load(f)

        if member == ctx.message.author and (self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot clear your own warns!")
        if self.bot.admin_role in member.roles and (self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot clear another staffer's warns")
        try:
            js.pop(str(member.id))
            await ctx.send("Cleared all of {}'s warns!".format(member.mention))
            emb = discord.Embed(title="Member Warns Cleared", colour=discord.Colour.orange())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
            with open("database/warns.json", "w") as f:
                json.dump(js, f, indent=2, separators=(',', ':'))
        except KeyError:
            return await ctx.send("This user doesn't have any warns!")





def setup(bot):
    bot.add_cog(Warn(bot))
