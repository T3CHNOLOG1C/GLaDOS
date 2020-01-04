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

    @commands.command(aliases=['ui'])
    async def userinfo(self, ctx, member: Union[Member, int, str] = None):
        """Prints userinfo on a member"""
        #print("\n----------------------------------------------------------------\n")

        inserver = None
        
        
        if member == None:
           # print('\n[DEBUG] Member is author\n')
            user = ctx.author
            inserver  = True

        elif isinstance(member, int):
           # print('\n[DEBUG] Member is an id')
            try:
              #  print("\nUser not found in server, searching api!\n")
                user = await self.bot.fetch_user(member)
                inserver = False
            except NotFound:
                await ctx.send(f"{self.femote} I cannot find that user")

        elif isinstance(member, Member):
          #  print("\n[DEBUG] discord member class detected")
            user = member
            inserver = True

        elif isinstance(member, str):
          #  print("\n[DEBUG] shitty error handling or smth")
            await ctx.send(f"{self.femote} I cannot find that user")
            return
        

        # is the user a bot?
        if user.bot:
            ubot = True
            
        else:
            ubot = False


        if inserver:
            
            uname = user.name
            uid = user.id
            udisrm = user.discriminator
            joindate = user.joined_at

            if user.activity == None:
                uacc = 'None'
            else:    
                uacc = user.activity.name
            unick = user.display_name
            sinner = user.premium_since
            ustat = user.status
            toprolecolor = user.color.value
            toprole = user.top_role
            createdate = user.created_at
            uavi = user.avatar_url
            udavi = user.default_avatar
           

            # embed or smth t3chgay
            embed = Embed(title=f'**Userinfo for {uname}#{str(udisrm)}**', color=toprolecolor)
            embed.description = f"**User's ID:** {str(uid)} \n **Join date:** {str(joindate)} \n **Created on** {str(createdate)} \n **Current Status:** {str(ustat).title()} \n **User Activity:**: {str(uacc)} \n **Default Profile Picture:** {str(udavi).title()} \n **Current Display Name:** {unick} \n **Nitro Boost Info:** {str(sinner)} \n **Current Top Role:** {str(toprole)} \n **Color:** {str(hex(toprolecolor)[2:])}"
            embed.set_thumbnail(url=uavi)
            if ubot:
                embed.set_footer(text=f"{uname} is a bot.")

            await ctx.send(embed=embed)

        elif inserver == False:
            uname = user.name
            uid = user.id
            udisrm = user.discriminator
            createdate = user.created_at
            uavi = user.avatar_url
            udavi = user.default_avatar

            embed = Embed(title=f'**Userinfo for {uname}#{str(udisrm)}**')
            embed.description = f"**User's ID:** {str(uid)} \n **Default Profile Picture:** {str(udavi)} \n  **Created on** {str(createdate)}"

            embed.set_footer(text=f'{uname} is not in your server.')
            embed.set_thumbnail(url=uavi)

            if ubot:
                embed.set_footer(text=f"{uname} is a bot and not on your server.")

            await ctx.send(embed=embed)

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
