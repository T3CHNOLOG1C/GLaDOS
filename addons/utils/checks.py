from discord.ext.commands import check


def _check_owner(ctx):
    return ctx.bot.owner_role in ctx.message.author.roles


def _check_botdev(ctx):
    return ctx.bot.botdev_role in ctx.message.author.roles or _check_owner(ctx)


def is_owner():
    return check(_check_owner)


def is_botdev():
    return check(_check_botdev)
