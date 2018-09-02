from discord.ext import commands


class Memes:
    """
    ayy lmao
    """

    def __init__(self, bot):
        self.bot = bot

    # SSS memes

    @commands.command()
    async def gudie(self, ctx):
        """Follow the Gudie to become a l33t Corbenik hax0r."""
        await ctx.send("https://gudie.racklab.xyz/")

    @commands.command()
    async def rip(self, ctx):
        """F"""
        msg = await ctx.send("Press F to pay respects.")
        await msg.add_reaction("🇫")

    @commands.command(aliases=["t3ch"])
    async def tech(self, ctx):
        """Goddamn Nazimod"""
        return await ctx.send("https://i.imgur.com/4kANai8.png")

    @commands.command()
    async def heil(self, ctx):
        """SIEG HEIL"""
        await ctx.send("HEIL T3CHNOLOG1C!")

    @commands.command()
    async def lenny(self, ctx):
        """( ͡° ͜ʖ ͡°)"""
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def brickdurr(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/hzuXOHP.png")

    @commands.command()
    async def birds(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/fVAx5oh.png")

    @commands.command()
    async def macboy(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/IpQC6IF.png")

    # SSS spammy-ish memes that need a cooldown
    @commands.cooldown(rate=1, per=30.0, type=commands.BucketType.channel)
    @commands.command(aliases=["astronautlevel"])
    async def astro(self, ctx):
        """MEMES???"""
        await ctx.send(
            "ASTRO DOES IT AGAIN!!!\n"
            "The peak nazi mod recuperance has occurred, mimicing the occurrence of 2016 where he "
            "once emotionally manipulated s_99 and xorhash to die off the server.\nIn that time, "
            "it was an emotionally draining period in which tensions were high and confusion was "
            "all over the place.\nThe word on the street places that this time is very similar "
            "to that time, in the dark days of the previously old, now defunct, 3d shacks, which "
            "was renamed to Nintendo Homebrew as of the final official takeover of Emma in late "
            "2016-early 2017, with the help of Ian.\nHowever, the old tales of his exploits have "
            "been sung across the land, and it is possible that they have led to influence over"
            "this most recent attempt of takeover of SSS.\nThe real quandry of all this "
            "however, is, how will he now react to the new role in taking over SSS?\nWill his "
            "potential ownership be riddeled with as much controversy as his old temporary "
            "ownership in 3dshacks? The future alone will know."
        )

    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def xkyup(self, ctx, variant: str=""):
        """
        MEMES???
        This meme has multiple variants : fr, es, it, jp, de, pl, pt, nl, se, bees
        You can also specify your own variant, and it will automatically generate a copypasta:
        I'm so sorry, I was a fucking retard for saying words that would get me in touble and
        anger lots of people who {} or who are dating {}.
        I didn't think before I spoke a word so it just came out as something totally wrong,
        I don't hate anybody who is {}, just the community. I like {}, just not the {} community.
        I'm sorry for all of this. All I'm asking for is a apology is all. I should have been
        thinking before I spoke."
        """
        if not variant:
            await ctx.send(
                "I'm so sorry, I was a fucking retard for saying words that would get me in touble"
                " and anger lots of people who are transgender or who are dating a transgender "
                "person. I didn't think before I spoke a word so it just came out as something "
                "totally wrong, I don't hate anybody who is transgender, just the community. I "
                "like Aurora, just not the trans community. I'm sorry for all of this. All I'm "
                "asking for is a apology is all. I should have been thinking before I spoke."
            )

        elif variant.lower() == "fr":
            await ctx.send(
                "Je suis tellement désolé, j'étais un putain d'attardé pour avoir dit des mots qui"
                " me mettraient dans le pétrin et qui mettraient beaucoup de personnes qui sont "
                "transgenres ou qui sont en couple avec une personne transgenre. Je n'ai pas "
                "réfléchi avant d'avoir dit un mot donc c'est juste sorti comme quelque chose de "
                "totalement faux, je ne déteste aucune personne transgenre, seulement la "
                "communauté. J'aime bien Aurora, juste pas la communauté trans. Je suis désolé "
                "pour tout ceci. Tout ce que je demande c'est des excuses, c'est tout. J'aurais du"
                " réfléchir avant de parler."
            )

        elif variant.lower() == "es":
            await ctx.send(
                "Estoy muy arrepentido, fui un estupido retardado por decir esas palabras que me "
                "pondrian en problemas y hacer enojar a mucha gente que son transexuales o que "
                "estan saliendo con una persona transexual. No pense antes de decir una palabra "
                "asi que salio como algo totalmente mal. Yo no odio cualquiera que sea transexual"
                ",solo la comunidad. Me gusta Aurora, solo no la trans comunidad. Estoy "
                "arrepentido por todo esto. Lo unico que pido es una disculpa. Tuve que haer "
                "pensado antes de hablar."
            )

        elif variant.lower() == "it":
            await ctx.send(
                "Mi dispiace così tanto, sono stato un fottuto idiota per aver detto cose che mi "
                "avrebbero messo nei guai e avrebbero fatto arrabbiare un sacco di persone che "
                "sono transgender o che stanno insieme ad una persona transgender. Non ho pensato "
                "prima di aprire bocca quindi è sembrato qualcosa di completamente sbagliato, non "
                "odio nessuno che sia transgender, solo la comunità. Mi piace Aurora, solo non l"
                "a comunità trans. Mi dispiace per tutto questo. Tutto ciò che sto chiedendo è di "
                "chiedere scusa, tutto qui. Avrei dovuto pensare prima di parlare."
            )

        elif variant.lower() == "jp":
            await ctx.send(
                "本当に申し訳ない, 私は多くのトランス人やトランス人をデートする人を怒らせる言葉で困ってしまった言葉を言ってからクソなリタードだった。 言葉を言った前に思った"
                "なかったから全く間違っていた何かを来た、誰でもトランスジェンダは嫌いじゃなくてあのコミュニティだけ嫌い。オーロラが好き、トランスのコミュニティだけではない。これは本"
                "当にすみません。私が求めているのは謝罪だけ。話す前に思っていたはずだった。"
            )

        elif variant.lower() == "de":
            await ctx.send(
                "Es tut mir sehr Leid, Ich war ein verfickter Behinderter als ich diese Worte sagte"
                " und wusste nicht wie sehr ich Ärger kriegen würde und wie sehr ich transsexuelle "
                "Menschen oder Menschen die transsexuelle daten erzörnen würde. Ich habe nicht "
                "gedacht bevor ich das Wort sagte und so kam es raus als was komplett falsches. "
                "Ich hasse keine Transsexuellen, nur die Gemeinschaft. Ich mag Transsexuelle, nur "
                "nicht die Gemeinschaft. Es tut mir sehr leid für all das. Ich bitte nur um "
                "Verzeihung. Ich hätte nachdenken sollen bevor ich den Mund aufgemacht habe."
            )

        elif variant.lower() == "pl":
            await ctx.send(
                "Bardzo mi przykro, byłem jebanym idiotą gdy wypowiedziałem te słowa i nie "
                "zdawałem sobie sprawy z tego jak bardzo naprzykrze sie osobom transseksualnym "
                "lub tym którzy chodzą z transseksualistami. Nie myślałem gdy wypowiedziałem te "
                "słowa i to co wyszło z moich ust było smutne i nieprawidłowe. Nic nie mam do osób"
                " trans, tylko do ich społeczności Lubie osoby trans, nie lubie tylko ich "
                "społeczności. Bardzo mi za to wszystko przykro. Proszę o przebaczenie. "
                "Powinienem był pomyśleć zanim cokolwiek napisałem."
            )

        elif variant.lower() == "pt":
            await ctx.send(
                "Peço imensa desculpa. Fui um grande retardado por dizer palavras que me iam meter"
                " em sarilhos com pessoas trans ou que estão a namorar com uma pessoa trans. "
                "Eu não pensei antes de falar por isso aquilo saiu como algo totalmente mau, eu "
                "não detesto ninguem que seja trans, só a comunidade trans. Eu gosto da Aurora, "
                "só não gosto da comunidade trans. Peço desculpa por tudo isto. Só peço que me "
                "desculpem. Devia ter pensado antes de ter falado."
            )

        elif variant.lower() == "nl":
            await ctx.send(
                "Het spijt me zo erg, ik was een echt achterlijk om woorden te zeggen die mij "
                "in moeite zou brengen en die veel mensen die transgender zijn of die in een "
                "relatie zijn met een transgender persoon boos zou maken. Ik heb niet nagedacht "
                "voor het spreken, dus kwam het als iets totaal vals, ik haat niemand die "
                "transgender is, alleen de gemeenschap. Ik hou van Aurora, alleen niet van de "
                "trans gemeenschap. Het spijt me voor dit alles. Alles what ik vraag is excuses, "
                "dat is alles. Ik had moeten denken voordat ik sprak"
            )

        elif variant.lower() == "se":
            await ctx.send(
                "hello guys im very sorry for punching a woman in discord chat. i do not "
                "understand what i do i am only muslim man coming to sweden from long "
                "country away i am very sorry this has been very sad and i only want "
                "apology so i do not bring shame on family that come sweden"
            )

        elif variant.lower() == "bees":
            await ctx.send(
                "I'm so sorry, I was a fucking retard for saying words that would get me in touble"
                " and anger lots of people who are bees or who are dating a bee. I didn't think "
                "before I spoke a word so it just came out as something totally wrong, I don't "
                "hate anybody who is a bee, just the hive. I like bees, just not the beehive. I'm "
                "sorry for all of this. All I'm asking for is a apology is all. "
                "I should have been thinking before I spoke."
            )

        else:
            try:
                variant = await commands.clean_content().convert(ctx, variant)
                words = variant.split(',')
                await ctx.send(
                    "I'm so sorry, I was a fucking retard for saying words that would get me in "
                    "touble and anger lots of people who {} or who are dating {}. I didn't think "
                    "before I spoke a word so it just came out as something totally wrong, I don't"
                    " hate anybody who is {}, just the community. I like {}, just not the {} "
                    "community. I'm sorry for all of this. All I'm asking for is a apology is all."
                    " I should have been thinking before I spoke."
                    "".format(words[0], words[1], words[2], words[3], words[4])
                )
            except IndexError:
                await ctx.send("Your syntax is incorrect. Please use the following syntax : "
                               "`.xkyup \"word1,word2,word3,word4,word5\"`. You must specify the 5"
                               " words.")
                return

    # Kurisu memes
    @commands.command()
    async def s_99(self, ctx):
        """Memes."""
        await ctx.send("**ALL HAIL BRITANNIA!**")

    @commands.command()
    async def dubyadud(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/Sohsi8s.png")

    @commands.command()
    async def rusure(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/dqh3fNi.png")

    @commands.command()
    async def permabrocked(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/ARsOh3p.jpg")

    @commands.command()
    async def thumbsup(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/hki1IIs.gifv")

    @commands.command()
    async def pbanjo(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/sBJKzuK.png")

    @commands.command()
    async def lisp(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/RQeZErU.png")

    @commands.command()
    async def blackalabi(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/JzFem4y.png")

    @commands.command()
    async def soghax(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/oQJy2eN.png")

    @commands.command()
    async def whatisr(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/Z8HhfzJ.jpg")

    @commands.command()
    async def sn0w(self, ctx):
        """Memes."""
        await ctx.send("http://i.imgur.com/sFD5uSB.png")

    @commands.command()
    async def helpers(self, ctx):
        """MEMES?"""
        await ctx.send("http://i.imgur.com/0v1EgMX.png")

    @commands.command()
    async def concern(self, ctx):
        """MEMES?"""
        await ctx.send("https://i.imgur.com/cWXBb5g.png")

    # GIB DONGRODER LAZY DEV
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def dongroder(self, ctx, variant=""):
        """MEMES?!?
        This meme has multiple variants : piter, swotch.
        If no variant is specified, it will defautlt to piter."""
        if variant == "piter":
            await ctx.send(
                "```Hey YOU. YES YOU!!!! YOU CAN CREATE A DOWNGRADER. JUST like can Plailect , "
                "Aurora Wright , astronautlevel and Apache Thunder and Kyojin work on a 3DS "
                "11.0 Downgrader!!!!!!!!!!!!!!!!!!!!!!!!!!!\nI mean I got arm11 acess with my "
                "6 copies of freakyforms deluxes and now i want to downgrade to 9.2 and as I have "
                "homebrew I can boot lima3ds but it doesnt boot its Aurora Wright fault, its "
                "incompetent and lazy to not develop for 11 I want downgrader to 9.2 and kernel "
                "exploit quick it's not hard ur the devs do it now quick.\nYou just have to "
                "hack/reprogram/patch the 11.0 FIRM so I can downgrade. Think the comunity. Cmon "
                "your hackers you acn do it. And plilect should make guide safer!!! becuase "
                "evryone bricks!!!!! And lima3ds should add nds rom support native. take notes "
                "Aurora Wright !!!!!!!!!!!!!!I WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI "
                "WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 "
                "DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI "
                "WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 "
                "DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI "
                "WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 "
                "DOWNGRADER NOW!!!!!!!!!!!!!!!\nI WANT 3DS 11.0 DOWNGRADER NOW!!!!!!!!!!!!!!!```"
            )
        elif variant == "swotch":
            await ctx.send(
                "```Hey YOU. YES YOU!!!! YOU CAN CREATE A DOWNGRADER. JUST like can Plailect , "
                "Aurora Wright , hedgeberg and SciresM and Daeken work on a Switch 3.0.2 "
                "dongroder!!!!!!!!!!!!!!!!!!!!!!!!!!!\nI mean I got browser acess with my 6 "
                "verzions of teh dns and now i want to downgrade to 3.0.0 and as I have browser I "
                "can boot reswotched but it doesnt boot teh hebrew lawnchair its Aurora Wright "
                "fault, its incompetent and lazy to not develop for 3.0.2 I want dongroder to "
                "3.0.0 and trustzone exploit quick it's not hard ur the devs do it now quick.\nYou"
                " just have to hack/reprogram/patch the 3.0.2 bootrom so I can dongrode. Think "
                "the comunity. Cmon your hackers you acn do it. And plilect should make swotch "
                "gudie safer!!! becuase evryone bricks!!!!! And limaswotch should add wii u rom "
                "support native. take notes Aurora Wright !!!!!!!!!!!!!!I WANT Switch 3.0.2 "
                "DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER "
                "NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT "
                "Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER "
                "NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT "
                "Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER "
                "NOW!!!!!!!!!!!!!!!\nI WANT Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!\nI WANT "
                "Switch 3.0.2 DONGROADER NOW!!!!!!!!!!!!!!!```"
            )

    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    @commands.command()
    async def gnulinux(self, ctx,):
        """GNU/Linux Copy Pasta"""
        await ctx.send("```I'd just like to interject for a moment. What you're referring to as "
                       "Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU"
                       " plus Linux. Linux is not an operating system unto itself, but rather "
                       "another free component of a fully functioning GNU system made useful by "
                       "the GNU corelibs, shell utilities and vital system components comprising "
                       "a full OS as defined by POSIX.\n\nMany computer users run a modified "
                       "version of the GNU system every day, without realizing it. "
                       "Through a peculiar turn of events, the version of GNU which is widely "
                       "used today is often called \"Linux\", and many of its users are not aware "
                       "that it is basically the GNU system, developed by the GNU Project.\n\n"
                       "There really is a Linux, and these people are using it, but it is just a "
                       "part of the system they use. Linux is the kernel: the program in the "
                       "system that allocates the machine's resources to the other programs that "
                       "you run. The kernel is an essential part of an operating system, but "
                       "useless by itself; it can only function in the context of a complete "
                       "operating system. Linux is normally used in combination with the GNU "
                       "operating system: the whole system is basically GNU with Linux added, "
                       "or GNU/Linux. All the so-called \"Linux\" distributions are really "
                       "distributions of GNU/Linux.```")

    @commands.command()
    async def kina(self, ctx):
        """kona"""
        await ctx.send("https://imgur.com/W3u6CoR")

    @commands.command()
    async def kina2(self, ctx):
        """Memes."""
        await ctx.send("http://imgur.com/8Mm5ZvB")

    @commands.command()
    async def beepbeep(self, ctx, *, roast: str="Roast"):
        """Bope"""
        roast = await commands.clean_content().convert(ctx, roast)
        await ctx.send("Your {} is ready".format(roast))

    @commands.command()
    async def themes(self, ctx):
        """S a l t"""
        await ctx.send("When it comes to custom theme managers on "
                       "the 3ds there haven't always been that "
                       "many choices\nI can only think of three "
                       "off the top of my head")


def setup(bot):
    bot.add_cog(Memes(bot))
