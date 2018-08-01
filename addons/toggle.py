import discord
from discord.ext import commands


class Toggle:
    """
    Toggle channel and role cmds (not colors)

    """

    def __init__(self, bot):
        self.bot = bot
        print("{} addon loaded".format(self.__class__.__name__))


    @commands.command(pass_context=True)
    async def togglechannel(self, ctx, channel):
        """Toggle access to some hidden channels"""

        user = ctx.message.author
        await ctx.message.delete()

        if channel == "nsfw":

            if self.bot.nsfw_role in user.roles:
                await user.remove_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels revoked.")
            else:
                await user.add_roles(self.bot.nsfw_role)
                await user.send("Access to NSFW channels granted.")
        else:
            await user.send("{} is not a togglable channel.".format(channel.replace('@everyone', '`@`everyone').replace('@here', '`@`here')))

    @commands.command(pass_context=True)
    async def togglerole(self, ctx, role=""):
        """toggle some hidden roles"""

        user = ctx.message.author
        joinmsg = "Joined {0} role"
        leavemsg = "Left {0} role"

        if role == "":
            embed = discord.Embed(title="Toggleable Roles:", color=discord.Color.dark_teal())
            embed.description = """
            - :race_car: Mario Kart 8 Deluxe: MK8D
            - :squid: Splatoon 2: spla2n
            - :card_box: Cards Against Humanity: cah
            - :bomb: Counter-Strike: Global Offensive: csgo
            - :gun: PUBG: pubg
            - :red_circle: Red Eclipse: redeclipse
            - :robot: Titanfall (2): titanfall
            - :boxing_glove: Super Smash Bros.: smash
            - :shopping_cart: Fortnite: fortnite
            """
            await ctx.send("", embed=embed)


        elif role.lower() == "mk8d":
            if self.bot.mk8d_role in user.roles:
                await user.remove_roles(self.bot.mk8d_role)
                await ctx.send(leavemsg.format(role.upper()))

            else:
                await user.add_roles(self.bot.mk8d_role)
                await ctx.send(joinmsg.format(role.upper()))

        elif role.lower() == "spla2n":
            if self.bot.spla2n_role in user.roles:
                await user.remove_roles(self.bot.spla2n_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.spla2n_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "cah":
            if self.bot.cah_role in user.roles:
                await user.remove_roles(self.bot.cah_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.cah_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "csgo":
            if self.bot.csgo_role in user.roles:
                await user.remove_roles(self.bot.csgo_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.csgo_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "pubg":
            if self.bot.pubg_role in user.roles:
                await user.remove_roles(self.bot.pubg_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.pubg_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "redeclipse":
            if self.bot.redeclipse_role in user.roles:
                await user.remove_roles(self.bot.redeclipse_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.redeclipse_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "titanfall":
            if self.bot.titanfall_role in user.roles:
                await user.remove_roles(self.bot.titanfall_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.titanfall_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "smash":
            if self.bot.smashbros_role in user.roles:
                await user.remove_roles(self.bot.smashbros_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.smashbros_role)
                await ctx.send(joinmsg.format(role.lower()))

        elif role.lower() == "fortnite":
            if self.bot.fortnite_role in user.roles:
                await user.remove_roles(self.bot.fortnite_role)
                await ctx.send(leavemsg.format(role.lower()))

            else:
                await user.add_roles(self.bot.fortnite_role)
                await ctx.send(joinmsg.format(role.lower()))
        else:
            msg = "{} is not a togglable role".format(role.replace('@everyone', '`@`everyone').replace('@here', '`@`here'))
            await ctx.send(msg)

def setup(bot):
    bot.add_cog(Toggle(bot))
