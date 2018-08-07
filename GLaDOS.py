from configparser import ConfigParser
from asyncio import sleep
from traceback import format_exception, format_exc
from json import load
from subprocess import run
from os import chdir, makedirs
from os.path import isfile, dirname, realpath
from sys import executable, exit as sysexit

import discord
from discord.ext import commands

# Change to script's directory
path = dirname(realpath(__file__))
chdir(path)

# Create database
makedirs("database", exist_ok=True)
if not isfile("database/warns.json"):
    with open("database/warns.json", "w") as f:
        f.write('{}')
if not isfile("database/ignored_users.json"):
    with open("database/ignored_users.json", "w") as f:
        f.write('{"users": []}')
if not isfile("database/emojif.json"):
    with open("database/emojif.json", "w") as f:
        f.write('{}')

bot_prefix = ["sudo ", "."]
bot = commands.Bot(command_prefix=bot_prefix, description="GLaDOS, a general purpose discord bot.",
                   max_messages=10000, pm_help=True)

# Read config.ini
config = ConfigParser()
config.read("config.ini")

@bot.event
async def on_ready():

    for guild in bot.guilds:
        bot.guild = guild

        # Moderation Roles
        bot.owner_role = discord.utils.get(guild.roles, name="Nazi Overlords (Owners)")
        bot.admin_role = discord.utils.get(guild.roles, name="Nazis (Admins)")
        bot.mod_role = discord.utils.get(guild.roles, name="Special Snowflakes (SS)")
        bot.staff_role = discord.utils.get(guild.roles, name="Staff")
        bot.botdev_role = discord.utils.get(guild.roles, name="BotDev")
        bot.nsfw_role = discord.utils.get(guild.roles, name="NSFW")
        bot.muted_role = discord.utils.get(guild.roles, name="Muted")
        bot.approved_role = discord.utils.get(guild.roles, name="Approved")


        # Game Roles
        bot.mk8d_role = discord.utils.get(guild.roles, name="MK8D")
        bot.csgo_role = discord.utils.get(guild.roles, name="CS: Russian Offensive")
        bot.pubg_role = discord.utils.get(guild.roles, name="pubg:battlebusters")
        bot.cah_role = discord.utils.get(guild.roles, name="CAH")
        bot.spla2n_role = discord.utils.get(guild.roles, name="Splatoon 2")
        bot.redeclipse_role = discord.utils.get(guild.roles, name="Red Eclipse")
        bot.titanfall_role = discord.utils.get(guild.roles, name="Titanfall")
        bot.smashbros_role = discord.utils.get(guild.roles, name="Super Smash Bros")
        bot.fortnite_role = discord.utils.get(guild.roles, name="Fort█▀█ █▄█ ▀█▀")


        # Color Roles
        bot.green_role = discord.utils.get(guild.roles, name="Green")
        bot.blue_role = discord.utils.get(guild.roles, name="Blue")
        bot.orange_role = discord.utils.get(guild.roles, name="Orange")
        bot.white_role = discord.utils.get(guild.roles, name="White")
        bot.black_role = discord.utils.get(guild.roles, name="Black")
        bot.sand_role = discord.utils.get(guild.roles, name="Sand")
        bot.pink_role = discord.utils.get(guild.roles, name="Pink")
        bot.teal_role = discord.utils.get(guild.roles, name="Teal")
        bot.red_role = discord.utils.get(guild.roles, name="Red")
        bot.purple_role = discord.utils.get(guild.roles, name="Purple")

        # Channels
        bot.announcements_channel = discord.utils.get(guild.channels, name="announcements")
        bot.botdev_channel = discord.utils.get(guild.channels, name="bot-dev")
        bot.botdms_channel = discord.utils.get(guild.channels, name="bot-dm")
        bot.logs_channel = discord.utils.get(guild.channels, name="admin-logs")
        bot.memberlogs_channel = discord.utils.get(guild.channels, name="member-logs")

    # Ignored users
    with open("database/ignored_users.json", "r") as f:
        ignored_users = load(f)["users"]
    bot.ignored_users = ignored_users

    # Load addons
    addons = [
        'addons.colors',
        'addons.emojif',
        'addons.events',
        'addons.memes',
        'addons.misc',
        'addons.mod',
        'addons.warn',
        'addons.speak',
        'addons.toggle',
    ]

    # Notify user if an addon fails to load.
    for addon in addons:
        try:
            bot.load_extension(addon)
        except Exception as e:
            print("Failed to load {} :\n{} : {}".format(addon, type(e).__name__, e))

    bot.all_ready = True

    print("Client logged in as {}, in the following guild : {}"
          "".format(bot.user.name, bot.guild.name))

# Handle errors
# Taken from
# https://github.com/916253/Kurisu/blob/31b1b747e0d839181162114a6e5731a3c58ee34f/run.py#L88
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        pass
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("{} You don't have permission to use this command."
                       "".format(ctx.message.author.mention))
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        formatter = commands.formatter.HelpFormatter()
        msg = await formatter.format_help_for(ctx, ctx.command)
        await ctx.send("{} You are missing required arguments.\n{}"
                       "".format(ctx.message.author.mention, msg[0]))
    elif isinstance(error, commands.errors.CommandOnCooldown):
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass
        message = await ctx.message.channel.send("{} This command was used {:.2f}s ago and is on "
                                                 "cooldown. Try again in {:.2f}s."
                                                 "".format(ctx.message.author.mention,
                                                           error.cooldown.per - error.retry_after,
                                                           error.retry_after))
        await sleep(10)
        await message.delete()
    else:
        await ctx.send("An error occured while processing the `{}` command."
                       "".format(ctx.command.name))
        print('Ignoring exception in command {0.command} in {0.message.channel}'.format(ctx))
        botdev_msg = "Exception occured in `{0.command}` in {0.message.channel.mention}".format(ctx)
        tb = format_exception(type(error), error, error.__traceback__)
        print(''.join(tb))
        botdev_channel = bot.botdev_channel
        await botdev_channel.send(botdev_msg + '\n```' + ''.join(tb) + '\n```')

@bot.event
async def on_error(ctx, event_method, *args, **kwargs):
    if isinstance(args[0], commands.errors.CommandNotFound):
        return
    elif isinstance(args[0], (commands.errors.MissingRequiredArgument, commands.errors.BadArgument)):
        helpm = await bot.formatter.format_help_for(ctx, ctx.command)
        for m in helpm:
            await ctx.send(m)
    elif isinstance(error, commands.CheckFailure):
        pass
    else:
        print('Ignoring exception in {}'.format(event_method))
        botdev_msg = "Exception occured in {}".format(event_method)
        tb = format_exc()
        print(''.join(tb))
        botdev_msg += '\n```' + ''.join(tb) + '\n```'
        botdev_msg += '\nargs: `{}`\n\nkwargs: `{}`'.format(args, kwargs)
        botdev_channel = bot.botdev_channel
        await botdev_channel.send(botdev_msg)
        print(args)
        print(kwargs)


# Core commands
@bot.command(hidden=True)
async def unload(ctx, addon: str):
    """Unloads an addon."""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        try:
            addon = "addons." + addon
            bot.unload_extension(addon)
            await ctx.send('✅ Addon unloaded.')
        except Exception as e:
            await ctx.send('💢 Error trying to unload the addon:\n```\n{}: {}\n```'
                           ''.format(type(e).__name__, e))

@bot.command(name='reload', aliases=['load'], hidden=True)
async def reload(ctx, addon: str):
    """(Re)loads an addon."""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        try:
            addon = "addons." + addon
            bot.unload_extension(addon)
            bot.load_extension(addon)
            await ctx.send('✅ Addon reloaded.')
        except Exception as e:
            await ctx.send('💢 Failed!\n```\n{}: {}\n```'.format(type(e).__name__, e))

            # Will add back later

@bot.command(hidden=True, name="pull", aliases=["pacman"])
async def pull(ctx, pip=None):
    """Pull new changes from Git and restart.
    Append -p or --pip to this command to also update python modules from requirements.txt."""
    dev = ctx.message.author
    if bot.botdev_role in dev.roles or bot.owner_role in dev.roles:
        await ctx.send("`Pulling changes...`")
        run(["git", "stash", "save"])
        run(["git", "pull"])
        run(["git", "stash", "clear"])
        pip_text = ""
        if pip in ("-p", "--pip", "-Syu"):
            await ctx.send("`Updating python dependencies...`")
            run([executable, "-m", "pip", "install", "--user",
                 "--upgrade", "-r", "requirements.txt"])
            pip_text = " and updated python dependencies"
        await ctx.send("Pulled changes{}! Restarting...".format(pip_text))
        run([executable, "GLaDOS.py"])
    else:
        if "pacman" in ctx.message.content:
            await ctx.send("`{} is not in the sudoers file. This incident will be reported.`"
                           "".format(ctx.message.author.display_name))
        else:
            await ctx.send("Only bot devs and / or owners can use this command")

@commands.has_permissions(administrator=True)
@bot.command()
async def restart(ctx):
    """Restart the bot (Staff Only)"""
    await ctx.send("`Restarting, please wait...`")
    run([executable, "GLaDOS.py"])

@commands.has_permissions(administrator=True)
@bot.command()
async def stop(ctx):
    """Stop the bot (Staff Only)"""
    await ctx.send("`Exiting...`")
    await bot.logout()

# Run the bot
if __name__ == "__main__":
    bot.run(config['Main']['token'])
