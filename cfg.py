#!/usr/bin/env python3.6
import configparser
import discord
from discord.ext import commands

# Read config.ini
config = configparser.ConfigParser()
config.read("config.ini")

bot_prefix = ["sudo", "."]
bot = commands.Bot(command_prefix=bot_prefix, description="GLaDOS, a general purpose discord bot.", max_messages=10000)

class cfg:
    """
    Bot Configuration Helper
    """

    for guild in bot.guilds:
        bot.guild = guild

    # Role Configuration Parsing
    preconfig_owner_role = config['Roles']['owner']
    preconfig_admin_role = config['Roles']['admin']
    preconfig_botdev_role = config['Roles']['botdev']
    preconfig_nsfw_role = config['Roles']['nsfw']
    preconfig_muted_role = config['Roles']['muted']


    # Roles
    bot.owner_role = discord.utils.get(guild.roles, name=preconfig_owner_role)
    bot.admin_role = discord.utils.get(guild.roles, name=preconfig_admin_role)
    bot.botdev_role = discord.utils.get(guild.roles, name=preconfig_botdev_role)
    bot.nsfw_role = discord.utils.get(guild.roles, name=preconfig_nsfw_role)
    bot.muted_role = discord.utils.get(guild.roles,name=preconfig_muted_role)

    # Channel Configuration Parsing
    preconfig_announcements_channel = config['Channels']['announcements']
    preconfig_botdev_channel = config['Channels']['botdev']
    preconfig_botdms_channel = config['Channels']['botdms']
    preconfig_adminlogs_channel = config['Channels']['adminlogs']

    # Channels
    bot.announcements_channel = discord.utils.get(guild.channels, name=preconfig_announcements_channel)
    bot.botdev_channel = discord.utils.get(guild.channels, name=preconfig_botdev_channel)
    bot.botdms_channel = discord.utils.get(guild.channels, name=preconfig_botdms_channel)
    bot.logs_channel = discord.utils.get(guild.channels, name=preconfig_adminlogs_channel)

def setup(bot):
    bot.add_cog(cfg(bot))
