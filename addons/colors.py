from discord.ext import commands


class Colors:
    """
    Color commands
    """

    def __init__(self, bot):
        self.bot = bot

    async def change(self, ctx, color, lang, cur_color, user):
        if not cur_color:
            await user.add_roles(color)
            await ctx.send("{} {} {} added."
                           "".format(user.mention, lang, color.name.lower()), delete_after=5)
        elif cur_color != color:
            await user.remove_roles(cur_color)
            await user.add_roles(color)
            await ctx.send("{} {} {} removed.\n"
                           "{} {} {} added."
                           "".format(user.mention, lang, cur_color.name.lower(),
                                     user.mention, lang, color.name.lower()), delete_after=5)
        else:
            await user.remove_roles(color)
            await ctx.send("{} {} {} removed."
                           "".format(user.mention, lang, color.name.lower()), delete_after=5)

    @commands.command(pass_context=True, aliases=['colour'])
    async def color(self, ctx, string=""):
        """Choose your colored role."""
        user = ctx.message.author
        await ctx.message.delete()
        lang = (ctx.invoked_with).capitalize()
        if not string:
            await ctx.send("{} You forgot to choose a {}!You can see the full list with `.list{}`"
                           "".format(user.mention, lang.lower(), lang.lower()), delete_after=10)
            return

        string = string.lower()

        colors = [
            self.bot.green_role,
            self.bot.blue_role,
            self.bot.orange_role,
            self.bot.white_role,
            self.bot.black_role,
            self.bot.sand_role,
            self.bot.pink_role,
            self.bot.teal_role,
            self.bot.red_role,
            self.bot.purple_role,
        ]
        applied_colors = []
        for color in colors:
            if color in user.roles:
                applied_colors.append(color)
        if applied_colors:
            cur_color = applied_colors[0]
        else:
            cur_color = None

        if string.lower() == "green":
            await self.change(ctx, self.bot.green_role, lang, cur_color, user)
        elif string.lower() == "blue":
            await self.change(ctx, self.bot.blue_role, lang, cur_color, user)
        elif string.lower() == "orange":
            await self.change(ctx, self.bot.orange_role, lang, cur_color, user)
        elif string.lower() == "white":
            await self.change(ctx, self.bot.white_role, lang, cur_color, user)
        elif string.lower() == "black":
            await self.change(ctx, self.bot.black_role, lang, cur_color, user)
        elif string.lower() == "sand":
            await self.change(ctx, self.bot.sand_role, lang, cur_color, user)
        elif string.lower() == "pink":
            await self.change(ctx, self.bot.pink_role, lang, cur_color, user)
        elif string.lower() == "teal":
            await self.change(ctx, self.bot.teal_role, lang, cur_color, user)
        elif string.lower() == "purple":
            await self.change(ctx, self.bot.purple_role, lang, cur_color, user)
        elif string.lower() == "red":
            await self.change(ctx, self.bot.red_role, lang, cur_color, user)
        else:
            await ctx.send("{} `{}` is not a permissible {}."
                           "".format(user.mention, string, lang), delete_after=5)

    @commands.command(pass_context=True, aliases=['listcolours', 'listcolor', 'listcolour'])
    async def listcolors(self, ctx):
        """List available colors"""
        await ctx.send(":art: **__{}ed roles:__**\n- green\n- blue\n- orange\n- white\n- black\n-"
                       "sand\n- pink\n- teal\n- red\n- purple\n"
                       "".format("Color" if ctx.invoked_with == "listcolor" or
                                 ctx.invoked_with == "listcolors" else "Colour"))


def setup(bot):
    bot.add_cog(Colors(bot))
