import qrcode
from discord.ext import commands
import discord
import io


class QRGen:
    """
    Module for generating QR codes from attachments and URLs
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qr(self, ctx, url=""):
        """Generate QR Code"""

        if url == "":
            async for m in ctx.channel.history():
                if len(m.attachments) == 1:  # Currently this only supports 1 attachment at most
                    img = qrcode.make(m.attachments[0].url)
                    imgbuf = io.BytesIO()
                    img.save(imgbuf, 'png')
                    imgbuf.seek(0)
                    await ctx.send(file=discord.File(imgbuf, "qr_code.png"))
                    return
        else:
            img = qrcode.make(url)
            imgbuf = io.BytesIO()
            img.save(imgbuf, 'png')
            imgbuf.seek(0)
            await ctx.send(file=discord.File(imgbuf, "qr_code.png"))


def setup(bot):
    bot.add_cog(QRGen(bot))
