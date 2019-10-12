from json import load, dump
from time import strftime, localtime

from discord import Member, Embed, Colour
from discord.ext import commands


class Warn(commands.Cog):
    """
    Warn commands
    """

    def __init__(self, bot):
        self.bot = bot

    async def dm(self, member: Member, message: str):
        """DM the user and catch an eventual exception."""
        try:
            await member.send(message)
        except:
            pass

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def warn(self, ctx, member: Member, *, reason: str=""):
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

        if member == ctx.message.author:
            await ctx.send("You cannot warn yourself!")
            return
        if self.bot.staff_role in member.roles and self.bot.owner_role not in author.roles:
            await ctx.send("You cannot warn other staff members!")
            return
        elif self.bot.owner_role in member.roles:
            await ctx.send("💢 I don't have the permission to do that!")
            return
        elif ctx.me is member:
            await ctx.send("I should not warn myself!")
            return

        try:
            with open("database/warns.json", "r") as config:
                js = load(config)
        except FileNotFoundError:
            with open("database/warns.json", "w") as config:
                config.write('{}')
                js = {}

        userid = str(member.id)
        if userid not in js:
            amount_of_warns = 1
            js[userid] = {"warns": []}
        else:
            amount_of_warns = len(js[userid]["warns"]) + 1

        member_name = "{}#{}".format(member.name, member.discriminator)
        timestamp = strftime("%Y-%m-%d %H:%M:%S", localtime())
        author_name = "{}#{}".format(author.name, author.discriminator)

        js[userid]["amount"] = amount_of_warns
        js[userid]["warns"].append({
            "name": member_name,
            "timestamp": timestamp,
            "reason": reason,
            "author": author_name,
            "author_id": author.id,
        })
        await ctx.send("🚩 I've warned {}. The user now has {} warns."
                       "".format(member, amount_of_warns))
        if reason == "":
            await self.dm(member, "You have been warned in {}.".format(ctx.guild.name))
        else:
            await self.dm(member, "You have been warned in {} for the following reason :\n{}\n"
                                  "".format(ctx.guild.name, reason))
        emb = Embed(title="Member Warned", colour=Colour.orange())
        emb.add_field(name="Member:", value=member, inline=True)
        emb.add_field(name="Warning Number:",
                      value=amount_of_warns, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
        if reason == "":
            reason = "No reason specified."
        emb.add_field(name="Reason:", value=reason, inline=True)
        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)

        if amount_of_warns == 1:
            await self.dm(member, "This is your first warning. "
                                  "The next warning will automatically mute you.")
        elif amount_of_warns == 2:
            await self.dm(member,
                          "This is your second warning, so you've been muted. You will be unmuted "
                          "whenever the admin who warned you decides to unmute you.\nYou will be "
                          "DM'ed when a mod unmutes you.\n**Do not ask mods to unmute you, as "
                          "doing so might extend the duration of the mute**")
            await self.dm(member, "Your next warn will result in being kicked from the server.")
            await member.add_roles(self.bot.muted_role)
        elif amount_of_warns == 3:
            await self.dm(member, "This is your third warning, so you have been kicked. Please "
                                  "note that **the next warn will result in another kick!**")
            await member.kick(reason="Third warn")
        elif amount_of_warns == 4:
            await self.dm(member, "You have been kicked from the server. This is your fourth and "
                                  "final warning. **__The next warning will result in an automatic"
                                  " permanent ban.__**")
            await member.kick(reason="Fourth warn")
        elif amount_of_warns >= 5:
            await self.dm(member, "You have reached your fifth warning. You are now permanently "
                                  "banned from this server.")
            await member.ban(delete_message_days=0, reason="Fifth warn.")

        with open("database/warns.json", "w") as f:
            dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))

    @commands.has_permissions(manage_roles=True)
    @commands.command(aliases=["unwarn", "delwarn"])
    async def deletewarn(self, ctx, member: Member, number: int):
        """
        Unwarn members. (Staff Only)
        A user ID can be used instead of mentionning the userself.
        """
        author = ctx.message.author
        if member == ctx.message.author:
            await ctx.send("You cannot remove a warn from yourself!")
            return
        if self.bot.staff_role in member.roles and self.bot.owner_role not in author.roles:
            await ctx.send("You cannot remove a warn from other staff members!")
            return
        elif self.bot.owner_role in member.roles:
            await ctx.send("💢 I don't have the permission to do that!")
            return
        elif number <= 0:
            await ctx.send("number has to be a positive number")
            return

        with open("database/warns.json", "r") as f:
            js = load(f)  # https://hastebin.com/ejizaxasav.scala

        userid = str(member.id)
        if userid not in js:
            js[userid] = {"warns": []}
            await ctx.send("{} doesn't have any warns.".format(member.name))
            return
        else:
            amount_of_warns = len(js[userid]["warns"]) - 1

        js[userid]["amount"] = amount_of_warns
        js[userid]["warns"].pop(number - 1)
        await ctx.send("🚩 I've deleted the {} warn of {}. The user now has {} warns."
                       "".format(number, member, amount_of_warns))
        await self.dm(member, "One of your warns in {} has been removed.".format(ctx.guild.name))
        emb = Embed(title="Member Unwarned", colour=Colour.orange())
        emb.add_field(name="Member:", value=member, inline=True)
        emb.add_field(name="Removed Warning Number:",
                      value=number, inline=True)
        emb.add_field(name="Mod:", value=ctx.message.author, inline=True)

        logchannel = self.bot.logs_channel
        await logchannel.send("", embed=emb)

        with open("database/warns.json", "w") as f:
            dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))

    @commands.command()
    async def listwarns(self, ctx, member: Member=None):
        """
        List your own warns or someone else's warns.
        Only the staff can view someone else's warns
        """
        if not member:
            member = ctx.message.author

        has_perms = self.bot.staff_role in ctx.message.author.roles

        if not has_perms and member != ctx.message.author:
            return await ctx.send("{} You don't have permission to list other member's warns!"
                                  "".format(ctx.message.author.mention))

        with open("database/warns.json", "r") as f:
            js = load(f)

        userid = str(member.id)
        if userid not in js:
            return await ctx.send("No warns found!")
        embed = Embed(color=member.colour)
        embed.set_author(name="List of warns for {} :".format(
            member), icon_url=member.avatar_url)

        for nbr, warn in enumerate(js[userid]["warns"]):
            content = "{}".format(warn["reason"])
            author = await self.bot.get_user_info(warn["author_id"])
            content += "\n*Warn author : {} ({})*".format(
                warn["author"], author.mention)
            embed.add_field(name="\n\n#{}: {}".format(nbr + 1, warn["timestamp"]),
                            value=content, inline=False)

        await ctx.send("", embed=embed)

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def clearwarns(self, ctx, member: Member):
        """Clear all of someone's warns. (Staff only)"""
        try:
            member = ctx.message.mentions[0]
        except IndexError:
            return await ctx.send("Please mention a user.")

        with open("database/warns.json", "r") as f:
            js = load(f)

        if member == ctx.message.author and (self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot clear your own warns!")
        if (self.bot.admin_role in member.roles and
                self.bot.owner_role not in ctx.message.author.roles):
            return await ctx.send("You cannot clear another staffer's warns")
        try:
            js.pop(str(member.id))
            await ctx.send("Cleared all of {}'s warns!".format(member.mention))
            emb = Embed(title="Member Warns Cleared", colour=Colour.orange())
            emb.add_field(name="Member:", value=member, inline=True)
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
            with open("database/warns.json", "w") as f:
                dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))
        except KeyError:
            return await ctx.send("This user doesn't have any warns!")


def setup(bot):
    bot.add_cog(Warn(bot))
