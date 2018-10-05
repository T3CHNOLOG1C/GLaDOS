from qrcode import make
from discord.ext import commands
from discord import File
from io import BytesIO


class QRGen:
    """
    Module for generating QR codes from attachments and URLs
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qr(self, ctx, url: str=None):
        """Generate QR Code"""

        if not url:
            async for m in ctx.channel.history():
                if len(m.attachments) == 1:  # Currently this only supports 1 attachment at most
                    img = make(m.attachments[0].url)
                    imgbuf = BytesIO()
                    img.save(imgbuf, 'png')
                    imgbuf.seek(0)
                    await ctx.send(file=File(imgbuf, "qr_code.png"))
                    return
        else:
            img = make(url)
            imgbuf = BytesIO()
            img.save(imgbuf, 'png')
            imgbuf.seek(0)
            await ctx.send(file=File(imgbuf, "qr_code.png"))


def setup(bot):
    bot.add_cog(QRGen(bot))
