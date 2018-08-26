from json import load, dump
from discord import TextChannel, errors, abc, Embed, Color
from discord.ext import commands


class Speak:
    """Give the bot a voice"""

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded.".format(self.__class__.__name__))

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def speak(self, ctx, destination: TextChannel, *, message: str):
        """Make the bot speak (Staff Only)"""
        await ctx.message.delete()
        await destination.send(message)
        try:
            emb = Embed(title="Message Sent", colour=Color.orange())
            emb.add_field(name="Mod:", value=ctx.message.author, inline=True)
            emb.add_field(name="Send from:", value=ctx.message.channel, inline=True)
            emb.add_field(name="Send To:", value=destination, inline=True)
            emb.add_field(name="Message:", value=message, inline=True)
            logchannel = self.bot.logs_channel
            await logchannel.send("", embed=emb)
        except errors.Forbidden:
            await ctx.send("💢 I dont have permission to do this.")

    async def memberDM(self, ctx, member, message):
        """Check for various parameters before DM'ing a member"""
        try:
            if ctx.message.attachments:
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
        except errors.Forbidden:
            await self.bot.logs_channel.send("Couldn't send message to {}.".format(member.mention))

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def dm(self, ctx, member, *, message=''):
        """DM a user. (Staff Only)"""

        member = ctx.message.mentions[0]
        await self.memberDM(ctx, member, message)
        author = ctx.message.author
        logOutput = "{} --> 📤 --> {} | \n".format(author, member)
        logOutput += "Message Content: {}".format(message)
        dmchannel = self.bot.botdms_channel
        await dmchannel.send(logOutput)

    # Log incoming dms if user is not ignored
    async def on_message(self, message):
        if isinstance(message.channel, abc.PrivateChannel):
            author = message.author
            if message.author.id == self.bot.user.id:
                pass
            elif message.author.id in self.bot.ignored_users:
                ignored_user_message = ("Sorry, your message `{}` could not be delivered due to "
                                        "you being blocked from messaging the bot. If you believe "
                                        "this is in error, too fucking bad."
                                        "".format(message.content))
                await author.send(ignored_user_message)
            else:
                dmchannel = self.bot.botdms_channel
                if message.attachments == []:
                    logOutput = "{} | {} 📨 {}\n".format(author, author.id, self.bot.user)
                    logOutput += "Message Content: {}".format(message.content)
                    await dmchannel.send(logOutput)
                else:
                    logOutput = "{} | {} 📨 {}\n".format(author, author.id, self.bot.user)
                    logOutput += "Message Content: {}\n".format(message.content)
                    logOutput += "Attachments: \n"
                    for attachment in message.attachments:
                        logOutput += "{}\n".format(attachment.url)
                    await dmchannel.send(logOutput)

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def ignore(self, ctx, member):
        """
        Ignore DM's from a user (Staff Only)
        If you use .ignore list, it will list all ignored members instead.
        """
        with open("database/ignored_users.json", "r") as f:
            js = load(f)

        if member == "list":
            if len(js["users"]) > 0:
                embed = Embed(title="List of ignored users", color=Color.blue())
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
                dump(js, f, indent=2, separators=(',', ':'))


def setup(bot):
    bot.add_cog(Speak(bot))

