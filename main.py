import discord
from discord.ext import commands
import logging
import random

class CuteGifs(commands.Cog):
    _lastHUG: int
    _hugs: list

    def __init__(self,bot) -> None:
        self.bot = bot
        self._hugs = []
        self._lastHUG = None
        self.__get_gifs()
        
    @commands.command()
    async def hug(self,ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        if len(ctx.message.mentions) == 0:
            return
        if len(self._hugs) < 1:
            await ctx.send("Command not available")
            return

        idx = random.randrange(len(self._hugs))
        while idx == self._lastHUG:
            idx = random.randrange(len(self._hugs))
        self._lastHUG = idx

        embed = discord.Embed()
        embed.set_image(url=self._hugs[idx])
        embed.color = 0x761cc9

        logging.info(f"{ctx.author.name} sent a hug via 'CuteGifs' command to {ctx.message.mentions[0].name}")

        await ctx.send(f"{ctx.author.mention} hugged {ctx.message.mentions[0].mention}!",embed=embed)

    def __get_gifs(self):
        self._hugs = []
        with open("hugs.txt") as file:
            for line in file:
                self._hugs.append(line)



def setup(bot):
    bot.add_cog(CuteGifs(bot))