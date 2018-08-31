from pylast import LastFMNetwork, LibreFMNetwork, WSError
from json import load, dump

from discord import errors, Member, Embed, Color
from discord.ext import commands

class LastFM:
    """
    """

    def __init__(self, bot):
        self.bot = bot
        try:
            with open("database/lastfm.json", "r") as config:
                self.config = load(config)
        except FileNotFoundError:
            self.config = {"users": {}, 'api': {'lastfm':['', ''], 'librefm':['', '']}}
            with open("database/lastfm.json", "w") as config:
                dump(self.config, config, indent=4, sort_keys=True, separators=(',', ':'))

        self.network = {}
        self.network['lastfm'] = LastFMNetwork(self.config['api']['lastfm'][0], self.config['api']['lastfm'][1])

        # TODO
        # get LibreFM working
        self.network['librefm'] = LibreFMNetwork()

    def isnetwork(self, value):
        cond1 = any(self.network[value].api_key)
        cond2 = any(self.network[value].api_secret)
        cond3 = any(self.network[value].username) # possibly used by LibreFMNetwork
        
        return cond1 and cond2 or cond3

    @commands.group(name="set")
    async def setservice(self, ctx):
        if ctx.invoked_subcommand is None:
            pages = await self.bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                await ctx.send(page)

    @setservice.command()
    async def lastfm(self, ctx, username):
        """Link your LastFM account to your Discord account"""
        try:
            self.network['lastfm'].get_user(username).get_now_playing()
            self.config['users'][str(ctx.message.author.id)] = username
            with open("database/lastfm.json", "w") as config:
                dump(self.config, config, indent=4, separators=(',', ':'))
            await ctx.send(f"Set your LastFM account to {username}")
        except WSError:
            if self.isnetwork('lastfm'):
                await ctx.send("User does not exist")
            else:
                await ctx.send("Addon has not been properly setup.")
                try:
                    emb = Embed(title = "LastFM", description = "Key or Secret not setup", colour = Color.orange())
                    logchannel = self.bot.logs_channel
                    await logchannel.send("", embed=emb)
                except errors.Forbidden:
                    await ctx.send("💢 I dont have permission to do this.")



    @setservice.command(hidden=True)
    async def librefm(self, ctx, username):
        await ctx.send("LibreFM support is still being worked on")

    @commands.command()
    async def np(self, ctx, user: Member = None):
        if not user:
            user = ctx.message.author

        try:
            account = self.network['lastfm'].get_user(self.config['users'][str(user.id)])
            playing = account.get_now_playing()
            if not playing:
                await ctx.send(f"{user.display_name} is playing nothing")
                return
            await ctx.send(f"{user.display_name} is playing {playing.artist.name} - {playing.title}")
        except KeyError as e:
            print("Failed to load:\n{} : {}".format(type(e).__name__, e))
            await ctx.send(f"You have no account\nPlease use `{ctx.prefix}set` to set one up")
        except WSError:
            await ctx.send(f"The account under your name is not available anymore.\nPlease use `{ctx.prefix}set` to set one up")


def setup(bot):
    bot.add_cog(LastFM(bot))
