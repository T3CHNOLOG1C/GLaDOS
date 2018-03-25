#!/usr/bin/env python3.6

import json
import re

import discord
from discord.ext import commands

class Emojif:

    """
    Replace the messages of non-nitro users that should contain animated
    emotes with the actual animated emote.
    """

    def __init__(self, bot):
        self.bot = bot
        with open("database/emojif.json", "r") as f:
            self.emojif_settings = json.load(f)
        try:
            self.emojif_active = False if self.emojif_settings['status'] is False else True
        except KeyError:
            self.emojif_active = True
        
        self.emojif_list = {}
        for g in bot.guilds:
            for e in g:
                if e.animated:
                    self.emojif_list[e.name] = e

        print("{} addon loaded.".format(self.__class__.__name__))

    @commands.group(name='emojif')
    async def emojif(self, ctx):
        """Manage Emojif"""

        if ctx.invoked_subcommand is None:
            return await ctx.send("No arguments. Please use .help emojif if you need help.")

    @emojif.command()
    async def toggle(self, ctx):
        """Opt in or out of Emojif."""

        member = str(ctx.message.author.id)
        with open("database/emojif.json", "r") as f:
            js = json.load(f)

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
            json.dump(js, f, indent=2, separators=(',', ':'))

        return await ctx.send("<@{}> {}".format(member, msg))

    @commands.has_permissions(administrator=True)
    @emojif.command()
    async def globaltoggle(self, ctx):
        """Globally enable or disable Emojif. (Mods only)"""

        with open("database/emojif.json", "r") as f:
            js = json.load(f)

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
            json.dump(js, f, indent=2, separators=(',', ':'))
        
        return await ctx.send(msg)

    async def on_message(self, message):
        """
        Replace messages that should contain animated emojis with
        their animated counterpart
        """

        return if not self.emojif_active:
        author = message.author
        try:
            return if author.bot or if not self.emojif_settings[author.id]
        except KeyError:
            return

        content = message.content
        imaginary_database = {'hey': 'hooooo'} # obviously replace this
        msg_emojis = re.findall(':\\w*:', content)
        for i, e in enumerate(msg_emojis):
            if e[1:-1] in imaginary_database:
                msg_emojis[i] = imaginary_database[e]
            else:
                msg_emojis.pop(i)
        if len(msg_emojis) == 0:
            return


        # At this point we can be sure that the message contains
        # an animated emoji, that the author isn't a bot,
        # that the user activated Emojifs for themselves and
        # that Emojifs are globally on. We can now format the message,
        # delete the original one, and post the new one.


        # Manage attachements / images
        # Post URL instead of saving then reuploading image,
        # to save time, bandwidth, and disk usage.
        if len(message.attachments) > 0:
            attachments = " ".join(attachment.url for attachment in ctx.message.attachments)
        else:
            attachments = ""
        formatted_author = "`{}`:".format(author.display_name)
        formatted_content = content.replace('@everyone', '`@everyone`').replace('@here', '`@here`')

        await message.delete()

        # Make sure the length of the message together with the length
        # of the attachments URLs don't go above the character limit.
        if len(attachments) + len(content) + len(formatted_author) + 2 > 3000:
            await message.channel.send("{} {}".format(formatted_author, formatted_content))
            await message.channel.send(attachments)
        else:
            await message.channel.send("{} {} {}".format(formatted_author, formatted_content, attachments))
  

        # TODO : => implement ram "cache" at init 
      

def setup(bot):
    bot.add_cog(Emojif(bot))

