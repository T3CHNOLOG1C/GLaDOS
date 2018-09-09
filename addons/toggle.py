from json import load, dump

from discord import Embed, Colour
from discord.ext import commands
from discord.utils import get


class Toggle:
    """
    Toggle channel and role commands (not colours)
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def togglechannel(self, ctx, channel):
        """Toggle access to some hidden channels"""

        user = ctx.message.author
        channel = await commands.clean_content().convert(ctx, channel)
        await ctx.message.delete()

        if channel == "nsfw":

            if self.bot.nsfw_role in user.roles:
                await user.remove_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels revoked.")
            else:
                await user.add_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels granted.")
        else:
            await user.send("{} is not a togglable channel.".format(channel))

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def addrole(self, ctx, keyword, emoji, role, *, description):
        """
        Add a new role to the bot's database, or replace one.
        If you don't need to link the role to a specific emoji,
        replace the "emoji" argument by "none".
        Role name is caps sensitive and must be between quotes.
        """

        try:
            with open("database/roles.json") as f:
                js = load(f)
        except FileNotFoundError:
            js = {}

        if emoji.lower() == "none":
            emoji = ""
        keyword = keyword.lower()

        js[keyword] = {}

        js[keyword]["emoji"] = emoji
        js[keyword]["role"] = role
        js[keyword]["description"] = description

        await ctx.send("Added role `{}` to the database.".format(keyword))

        with open("database/roles.json", "w") as f:
            dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def delrole(self, ctx, keyword):
        """
        Delete a role from the bot's database
        """

        try:
            with open("database/roles.json") as f:
                js = load(f)
        except FileNotFoundError:
            js = {}

        try:
            del js[keyword]
        except KeyError:
            await ctx.send("This role is not in the database!")
            return

        with open("database/roles.json", "w") as f:
            dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))

    @commands.command()
    async def togglerole(self, ctx, keyword=""):
        """
        Toggle some opt-in roles
        """

        user = ctx.message.author
        keyword = keyword.lower()

        try:
            with open("database/roles.json") as f:
                js = load(f)
        except FileNotFoundError:
            js = {}

        try:
            rolename = js[keyword]["role"]
            role = get(ctx.message.guild.roles, name=rolename)
            if role in user.roles:
                await user.remove_roles(role)
                await ctx.send("Left {}".format(rolename))
                return
            await user.add_roles(role)
            await ctx.send("Joined {}".format(rolename))

        except KeyError:
            if keyword == "":
                embed = Embed(title="List of toggleable roles:",
                              colour=Colour.dark_teal())
                embed.description = ""
                for k in js:
                    embed.description += "- {} {}: `{}`\n".format(
                        js[k]["emoji"],
                        js[k]["description"],
                        k
                    )
                await ctx.send("", embed=embed)
                return

            await ctx.send("This role is not in the database!")


def setup(bot):
    bot.add_cog(Toggle(bot))
