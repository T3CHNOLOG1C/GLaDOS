#!/usr/bin/env python3

from discord import Member, Embed, Colour, errors
from discord.ext import commands

class Moderation:
    """
    Moderation commands
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

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: Member = None, *, reason: str = ""):
        """Kick a member. (Staff Only)"""
        try:
            if not member:
                if ctx.message.author == owner:
                    return await ctx.send("Yes daddy t3ch?")
                else:
                    return await ctx.send("Please mention a user.")
            if member == ctx.message.author:
                return await ctx.send("You cannot kick yourself!")
            if (self.bot.admin_role in member.roles and
                    self.bot.owner_role not in ctx.message.author.roles):
                return await ctx.send("You may not kick another staffer")
            if reason == "":
                dm_msg = "You have been kicked from {}.".format(ctx.guild.name)
            else:
                dm_msg = ("You have been kicked from {} for the following reason:\n{}"
                          "".format(ctx.guild.name, reason))
            await self.dm(member, dm_msg)
            await member.kick()
            await ctx.send("I've kicked {}.".format(member))
            emb = Embed(title="Member Kicked", colour=Colour.red())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            if reason == "":
                reason = "No reason specified."
            emb.add_field(name="Reason:", value=reason, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: Member = None, *, reason: str = ""):
        """Ban a member. (Staff Only)"""
        if not member:
            if ctx.message.author == owner:
                return await ctx.send("Yes daddy t3ch?")
            else:
                return await ctx.send("Please mention a user.")
        if member == ctx.message.author:
            return await ctx.send("You cannot ban yourself!")
        if (self.bot.admin_role in member.roles and
                self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You may not ban another staffer")
        else:
            try:
                if not reason:
                    dm_msg = "You have been banned from {}.".format(ctx.guild.name)
                else:
                    dm_msg = ("You have been banned from {} for the following reason:\n{}"
                              "".format(ctx.guild.name, reason))
                await self.dm(member, dm_msg)
                await member.ban(delete_message_days=0)
                await ctx.send("I've banned {}.".format(member))
                emb = Embed(title="Member Banned", colour=Colour.red())
                emb.add_field(name="Member:", value=member.name, inline=True)
                emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
                if reason == "":
                    reason = "No reason specified."
                emb.add_field(name="Reason:", value=reason, inline=True)
                logchannel = self.bot.logs_channel
                await logchannel.send("", embed=emb)
            except errors.Forbidden:
                await ctx.send("💢 I dont have permission to do this.")

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def lockdown(self, ctx, *, reason=""):
        """
        Lock down a channel
        """
        channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        if reason == "":
            await channel.send(":lock: Channel locked.")
        else:
            await channel.send(":lock: Channel locked. The given reason is: {}".format(reason))
        emb = Embed(title="Lockdown", colour=Colour.gold())
        ch = "{} ({})".format(ctx.channel.mention, ctx.channel.name)
        emb.add_field(name="Channel:", value=ch, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
        if reason == "":
            reason = "No reason specified."
        emb.add_field(name="Reason:", value=reason, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def unlock(self, ctx):
        """
        Unlock a channel
        """
        channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await channel.send(":unlock: Channel Unlocked")
        emb = Embed(title="Unlock", colour=Colour.gold())
        ch = "{} ({})".format(ctx.channel.mention, ctx.channel.name)
        emb.add_field(name="Channel:", value=ch, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author.name, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)

    # WARN STUFF moved to warn.py

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def approve(self, ctx, member):
        """Approve members"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")
        if self.bot.approved_role not in member.roles:
            try:
                await member.add_roles(self.bot.approved_role)
                dm_msg = "You have been approved. Welcome to {}!".format(ctx.guild.name)
                await self.dm(member, dm_msg)
                await ctx.send(":thumbsup: {} has been approved".format(member))
                emb = Embed(title="Member Approved", colour=Colour.blue())
                emb.add_field(name="Member:", value=member, inline=True)
                emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
                logchannel = self.bot.logs_channel
                await logchannel.send("", embed=emb)
            except errors.Forbidden:
                await ctx.send("💢 I dont have permission to do this.")
        elif self.bot.approved_role in member.roles:
            await ctx.send("{} is already approved!".format(member))

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, member, *, reason=""):
        """Mutes a user. (Staff Only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")

        if member == ctx.message.author and (self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot mute yourself!")
        if (self.bot.admin_role in member.roles and
                self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot mute other staffers!")

        if self.bot.muted_role in member.roles:
            return await ctx.send("{} is already muted!".format(member))

        try:
            await member.add_roles(self.bot.muted_role)
            await ctx.send("{} can no longer speak!".format(member))
            if not reason:
                msg = ("You have been muted in {} by {}. You will be DM'ed when a mod unmutes you."
                       "\n**Do not ask mods to unmute you, as doing so might extend the duration "
                       "of the mute**".format(ctx.guild.name, ctx.message.author))
            else:
                msg = ("You have been muted in {} by {}. The given reason is {}. You will be DM'ed"
                       " when a mod unmutes you.\n**Do not ask mods to unmute you, as doing so "
                       "might extend the duration of the mute**"
                       "".format(ctx.guild.name, ctx.message.author, reason))
            await self.dm(member, msg)
            emb = Embed(title="Member Muted", colour=Colour.purple())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            if reason == "":
                emb.add_field(name="Reason:", value="No reason specified.", inline=True)
            else:
                emb.add_field(name="Reason:", value=reason, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def unmute(self, ctx, member):
        """Unmutes a user. (Staff Only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")


        if (self.bot.admin_role in member.roles and
                self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot unmute other staffers!")

        try:
            if self.bot.muted_role not in member.roles:
                return await ctx.send("{} is not muted!".format(member))
            if member == ctx.message.author:
                return await ctx.send("You cannot unmute yourself! "
                                      "How did you even manage to send this if you are muted?")
            await member.remove_roles(self.bot.muted_role)
            await ctx.send("{} is no longer muted!".format(member))
            msg = "You have been unmuted in {}.".format(ctx.guild.name)
            await self.dm(member, msg)
            emb = Embed(title="Member Unmuted", colour=Colour.purple())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")




def setup(bot):
    bot.add_cog(Moderation(bot))
