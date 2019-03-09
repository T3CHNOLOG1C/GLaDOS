from json import load, dump
from re import findall

from discord.utils import get
from discord.ext import commands


class Emojif(commands.Cog):

    """
    Replace the messages of non-nitro users that should contain animated
    emotes with the actual animated emote.
    """

    def __init__(self, bot):
        self.bot = bot
        try:
            with open("database/emojif.json") as f:
                self.emojif_settings = load(f)
        except FileNotFoundError:
            with open("database/emojif.json", "w") as f:
                f.write('{}')
        try:
            self.emojif_active = self.emojif_settings['status']
        except KeyError:
            self.emojif_active = True

    @commands.group(name='emojif')
    async def emojif(self, ctx):
        """Manage Emojif"""

        if ctx.invoked_subcommand is None:
            return await ctx.send("No arguments. Please use .help emojif if you need help.")

    @emojif.command()
    async def toggle(self, ctx):
        """Opt in or out of Emojif."""

        member = str(ctx.message.author.id)
        try:
            with open("database/emojif.json") as f:
                js = load(f)
        except FileNotFoundError:
            js = {}

        try:
            if js[member]:
                js[member] = False
                self.emojif_settings[member] = False
                msg = "Your messages containing animated emotes will no longer be replaced."
            else:
                js[member] = True
                self.emojif_settings[member] = True
                msg = "Your messages containing animated emotes will now be replaced."
        except KeyError:
            js[member] = True
            self.emojif_settings[member] = True
            msg = "Your messages containing animated emotes will now be replaced."

        with open("database/emojif.json", "w") as f:
            dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))

        return await ctx.send("<@{}> {}".format(member, msg))

    @emojif.command()
    async def list(self, ctx):
        """List all animated emojis that the bot can use."""

        output = ""
        for e in self.bot.emojis:
            if not e.animated:
                continue
            output += '**`:{}:`** -> {}\n'.format(e.name, str(e))
        await ctx.send("__List of animated emojis :__\n\n" + output)

    @commands.has_permissions(administrator=True)
    @emojif.command()
    async def globaltoggle(self, ctx):
        """Globally enable or disable Emojif. (Mods only)"""

        try:
            with open("database/emojif.json") as f:
                js = load(f)
        except FileNotFoundError:
            js = {}

        try:
            if js['status']:
                js['status'] = False
                self.emojif_active = False
                msg = "Emojif is now globally disabled."
            else:
                js['status'] = True
                self.emojif_active = True
                msg = "Emojif is now globally enabled."
        except KeyError:
            js['status'] = False
            self.emojif_active = False
            msg = "Emojif is now globally disabled."

        with open("database/emojif.json", "w") as f:
            dump(js, f, sort_keys=True, indent=4, separators=(',', ': '))

        return await ctx.send(msg)

    async def on_message(self, message):
        """
        Replace messages that should contain animated emojis with
        their animated counterpart
        """

        if self.emojif_active is False:
            return
        author = message.author
        try:
            if author.bot is True or self.emojif_settings[str(author.id)] is False:
                return
        except KeyError:
            return

        content = message.content
        msg_emojis = findall(':\\w+:', content)
        client_emojis = tuple(e.name for e in self.bot.emojis if e.animated)
        for i, e in enumerate(msg_emojis):
            if e[1:-1] not in client_emojis:
                msg_emojis.pop(i)
        if not msg_emojis:
            return

        # At this point we can be sure that the message contains
        # a server emoji, that the author isn't a bot,
        # that the user activated Emojifs for themselves and
        # that Emojifs are globally on. We can now format the message,
        # delete the original one, and post the new one.

        # Manage attachements / images
        # Post URL instead of saving then reuploading image,
        # to save time, bandwidth, and disk usage.
        if not message.attachments:
            attachments = " ".join(
                attachment.url for attachment in message.attachments)
        else:
            attachments = ""
        formatted_author = "`{}`:".format(author.display_name)
        formatted_content = content.replace(
            '@everyone', '`@`everyone').replace('@here', '`@`here')
        animated_emojis = []
        for e in set(msg_emojis):
            found_emoji = get(self.bot.emojis, name=e[1:-1])
            formatted_content = formatted_content.replace(e, str(found_emoji))
            if found_emoji.animated:
                animated_emojis.append(found_emoji)

        # Make sure the message contains at least one animated emoji
        if not animated_emojis:
            return

        await message.delete()

        # Make sure the length of the message together with the length
        # of the attachments URLs don't go above the character limit.
        if len(attachments) + len(content) + len(formatted_author) + 2 > 3000:
            await message.channel.send("{} {}".format(formatted_author, formatted_content))
            await message.channel.send(attachments)
        else:
            await message.channel.send("{} {} {}".format(formatted_author, formatted_content,
                                                         attachments))


def setup(bot):
    bot.add_cog(Emojif(bot))
