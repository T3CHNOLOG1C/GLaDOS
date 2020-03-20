import discord
import os
import json
import asyncio
from discord.ext import commands
from typing import Union


class AccountInfo(commands.Cog):
    """fill this in later, am lazy"""

    def __init__(self, bot):
        self.bot = bot
        self.database = {}
        self.filename = 'database/accounts.json'
        self.semote = '👍'
        self.femote = '💢'


    # json interation commands

    def readJson(self):
        """Reads our json file"""
        
        if self.checkFile(self.filename):
            with open(self.filename) as f:
                self.database = json.load(f)
            
        else:
            with open(self.filename, 'w') as f:
                json.dump({}, f)
            
            #self.readjson() # Check has failed, trying again after creating the file!
        
    def writeJson(self):
        """Writes our database to our json file"""
        if self.checkFile(self.filename):
            with open(self.filename, 'w') as f:
                json.dump(self.database, f, indent=4)
        
        else:
            self.readJson()
    
    # Checks

    def checkFile(self, file):
        """Very simple function to check to see if a file exists and if its empty"""
        if os.path.isfile(file):
            size = os.stat(file).st_size
            if size == 0:
                return False
            
            else:
                return True
        
        else:
            return False

    def checkuser(self, user):
        """Checks to see if a user is in the database"""
        # To be called after reading the json file
        if user in self.database:
            return True
        
        else:
            return False

    async def fcCheck(self, ctx, accType, accData):
        """Verifies 3ds and switch friend codes"""

        if accType.lower() == 'switch' or accType.lower() == '3ds':
            if len(accData) == 14:
                return True

            else:
                await ctx.send(f"{self.femote} That is an invalid {accType} friend code! Please make sure you enter  your {accType} friend code is entered like `xxxx-xxxx-xxxx`")
                return False
                
        else:
            return True

    def dbEntryCheck(self, user, accType):
        """Checks to see if an account exists"""
        
        if accType in self.database[user].keys():
            return True
        
        else:
            return False
        


    async def argExist(self, ctx, acc, accdata):
        """Checker to see if a user has enter the args"""

        if acc == None:
            await ctx.send(f"{self.femote} No argument entered, please make sure to enter what kind of account you want to add!")
            return False
        
        elif accdata == None:
            await ctx.send(f"{self.femote} No arguemt entered, please make sure you enter your account name!")
            return False

       
        return True

    async def argLimit(self, ctx, acc, accData):

        if len(acc) > 30:
            await ctx.send(f"{self.femote} Your account type name is too long!")
            return False

        elif len(accData) > 120:
            await ctx.send(f"{self.femote} Your account username is too long!")
            return False

        elif acc.isspace() or accData.isspace() or acc == "" or accData == "\n":
            await ctx.send("You wanna be slapped?")
            return False
        
        else:
            return True

    async def rolecolor(self, ctx, member: discord.Member = None):
        """Gets the highest role for a member"""
        
        mcolor = member.color.value
        return mcolor
        
    
        
    # discord commands



    @commands.command(aliases=['aa','addacc'])
    async def accountadd(self, ctx, acc = None, *, accdata = None):
        """Adds an account to the database"""
        self.readJson()
    
        user = ctx.author
        
        uid = str(user.id)

        if self.checkuser(uid):
            pass


        else:
            self.database[uid] = {}
            self.writeJson()
            pass
        
    
        # lets add the accounts
        # error handling is handled by the function in the if statement, pass is used to stop the command
        if not await self.argExist(ctx, acc, accdata):
            pass

        elif not await self.fcCheck(ctx, acc, accdata):
            pass
        
        elif not await self.argLimit(ctx, acc, accdata):
            pass

        else:
            self.database[uid][acc] = accdata
            self.writeJson()
            if acc.lower() == 'switch' or acc.lower() == '3ds':
                await ctx.send(f"Adding your {acc} friend code: {accdata} {self.semote}")
            
            else:
                await ctx.send(discord.utils.escape_mentions(f"Adding your {acc} account: {accdata} {self.semote}"))
            self.database = {}


        
    @commands.command(aliases=['delacc'])
    async def accountdelete(self, ctx, acc = None):
        """Command to delete an account from the database"""
        user = ctx.author
        uid = str(user.id)
        self.readJson()

        if self.checkuser(uid):
            pass

        else:
            self.database[uid] = {}
            self.writeJson()
            
        
        # the account element
        if acc == None:
            accdata = None

        else:
            accdata = self.database[uid][acc]

        if not await self.argExist(ctx, acc, accdata):
           pass
        
        elif not await self.argLimit(ctx, acc, accdata):
            pass

        elif not self.dbEntryCheck(uid, acc):
            if acc.lower() == 'switch' or acc.lower() == '3ds':
                await ctx.send(f"{self.femote} You do not have a {acc} friend code saved!")

            else:
                await ctx.send(f"{self.femote} You do not have a {acc} account saved")  
        
        else:
            del self.database[uid][acc]
            self.writeJson()

            if acc.lower() == 'switch' or acc.lower() == '3ds':
                await ctx.send(f"Successfully deleted your {acc} friend code from the database {self.semote}")
            
            else:
                await ctx.send(discord.utils.escape_mentions(f"Successfully delete your {acc} account from the database {self.semote}"))

            self.database = {}

        
    @commands.command(aliases=['updateacc', 'ua'])
    async def updateaccount(self, ctx, acc = None, newacc = None):
        """Update an account in the database"""

        user = ctx.author
        uid = str(user.id)
        self.readJson()

        if self.checkuser(uid):
            pass


        else:
            self.database[uid] = {}
            self.writeJson()

        # the account element

        if acc == None:
            newacc = None
        
        
        # function in the if statement handles output, pass ends the command!
        if not await self.argExist(ctx, acc, newacc):
           pass
        
        elif not await self.fcCheck(ctx, acc, newacc):
            pass
        
        elif not await self.argLimit(ctx, acc, newacc):
            pass
       
        elif not self.dbEntryCheck(uid, acc):
            if acc.lower() == 'switch' or acc.lower() == '3ds':
                await ctx.send(f"{self.femote} You do not have a {acc} friend code saved!")

            else:
                await ctx.send(f"{self.femote} You do not have a {acc} account saved")

        else:
            #print(self.database)
            self.database[uid][acc] = newacc
            print(f"\n {newacc} \n")
            print(self.database)
            self.writeJson()
            if acc.lower() == 'switch' or acc.lower() == '3ds':
                await ctx.send(f"{acc} friend code has been updated {self.semote}")
            
            else:
                await ctx.send(f"{acc} account has been updated {self.semote}")
            
            self.database = {}


    @commands.command(aliases=['le'])
    async def listentries(self, ctx, member = None):
        """Lists database entries for a user"""

        if member == None:
            user = ctx.author

        else:
            try:
                user = await commands.MemberConverter().convert(ctx, member)

            except commands.BadArgument:
                await ctx.send("💢 I cannot find that user!")
                return
            
            except KeyError:
                await ctx.send("💢 I cannot find that user!")
                return

        self.readJson()
        uid = str(user.id)
        embed = discord.Embed(title=f"Accounts for {user.name}#{str(user.discriminator)}", color=await self.rolecolor(ctx, user))
        try:
            totalacc =  len(self.database[uid])
        except KeyError:
            pass
        if uid in self.database:
            for account in self.database[uid]:
                embed.add_field(name=account, value=self.database[uid][account], inline=False)
            
            embed.set_footer(text=f'{totalacc} total accounts')
            await ctx.send(embed=embed)

        else:
            await ctx.send(f"{self.femote} This user has no entries")      

def setup(bot):
    bot.add_cog(AccountInfo(bot))