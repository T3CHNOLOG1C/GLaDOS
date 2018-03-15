#!/usr/bin/python3.6
import json
import discord
from discord.ext import commands

class Speak:
    """Give the bot a voice"""

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))
        


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def speak(self, ctx, destination, *, message):
        """Make the bot speak (Staff Only)"""
        await ctx.message.delete()
        if len(ctx.message.channel_mentions) > 0:
            channel = ctx.message.channel_mentions[0]
            await channel.send(message)

    async def memberDM(self, ctx, member, message):
        """Check for various parameters before DM'ing a member"""
        try:
            if len(ctx.message.attachments) > 0:
                attachments = " ".join(attachment.url for attachment in ctx.message.attachments)
                message = "{} {}".format(message, attachments)
            else:
                if message == '':
                    return await ctx.send("You cannot send empty messages!")
                else:
                    await ctx.message.delete()
            if len(message) > 2000:
                await member.send(message[:2000])
                await member.send(message[2000:])
            else:
                await member.send(message)
        except discord.errors.Forbidden:
            await self.bot.logs_channel.send("Couldn't send message to {}.".format(member.mention))

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def dm(self, ctx, member, *, message=''):
        """DM a user. (Staff Only)"""

        member = ctx.message.mentions[0]
        await self.memberDM(ctx, member, message)
        author = ctx.message.author
        logOutput = "{} --> 📤 --> {}\n".format(author, member)
        logOutput += "Message Content: {}".format(message)
        dmchannel = discord.utils.get(bot.guild.channels, name=preconfig_botdev_channel)
        await dmchannel.send(logOutput)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def answer(self, ctx, *, message=''):
        """Answer to the latest DM (Staff Only)"""

        async for m in self.bot.botdms_channel.history(limit=250):
                try:
                    if m.author == self.bot.user:
                        member = m.mentions[0]
                        break
                    else:
                        continue
                except IndexError:
                    continue
        await self.memberDM(ctx, member, message)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def ignore(self, ctx, member):
        """
        Ignore DM's from a user (Staff Only)
        If you use .ignore list, it will list all ignored members instead.
        """
        with open("database/ignored_users.json", "r") as f:
            js = json.load(f)

        if member == "list":
            if len(js["users"]) > 0:
                embed = discord.Embed(title="List of ignored users", color=discord.Color.blue())
                ignored_users = []
                for i in js["users"]:
                    u = self.bot.get_user(i)
                    ignored_users.append(u)
                description = ""
                for u in ignored_users:
                    description += "- {} ({})\n".format(u, u.mention)
                embed.description = description
                return await ctx.send("", embed=embed)
            else:
                return await ctx.send("There are no ignored users!")
        else:
            try:
                member = ctx.message.mentions[0]
            except IndexError:
                await ctx.send("Please mention a user.")
            if member.id in js["users"]:
                js["users"].remove(member.id)
                self.bot.ignored_users.remove(member.id)
                await ctx.send("Removed {} from ignored users.".format(member.mention))
            else:
                js["users"].append(member.id)
                self.bot.ignored_users.append(member.id)
                await ctx.send("Added {} to ignored users.".format(member.mention))
            with open("database/ignored_users.json", "w") as f:
                json.dump(js, f, indent=2, separators=(',', ':'))


def setup(bot):
    bot.add_cog(Speak(bot))
