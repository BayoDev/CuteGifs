import nextcord
from nextcord.ext import commands
import logging
import random
import os

TESTING_GUILDS = []

class CuteGifs(commands.Cog):

    _lastHUG: int
    _hugs: list

    _lastPAT: int
    _pats: list

    _lastKISS: int
    _kisses: list

    _path: str
    _config : dict

    def __init__(self,bot,config) -> None:
        self._bot = bot
        self._path = os.getcwd()
        self._config = config

        self.__get_gifs()
        self.__get_kisses()
        self.__get_pats()

    def __get_gifs(self):
        if not os.path.isfile('hugs.txt'):
            with open('hugs.txt','w') as file:
                file.write(" ")
                logging.info("hugs.txt file created. Add gifs to the file to use the command")
                return
        self._lastHUG = None
        self._hugs = []
        with open("hugs.txt") as file:
            for line in file:
                self._hugs.append(line)

    def __get_kisses(self):
        if not os.path.isfile('kisses.txt'):
            with open('kisses.txt','w') as file:
                file.write(" ")
                logging.info("kisses.txt file created. Add gifs to the file to use the command")
        self._lastKISS = None
        self._kisses = []
        with open("kisses.txt") as file:
            for line in file:
                self._kisses.append(line)

    def __get_pats(self):
        if not os.path.isfile('pats.txt'):
            with open('pats.txt','w') as file:
                file.write(" ")
                logging.info("pats.txt file created. Add gifs to the file to use the command")
        self._lastPAT = None
        self._pats = []
        with open("pats.txt") as file:
            for line in file:
                self._pats.append(line)

    @nextcord.slash_command(
        name='hug',
        description='Send a hug to a user',
        guild_ids= TESTING_GUILDS
    )
    async def hug(self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(name='user',description='user to hug',required=True)
    ):

        idx = random.randrange(len(self._hugs))
        while idx == self._lastHUG:
            idx = random.randrange(len(self._hugs))
        self._lastHUG = idx

        embed = nextcord.Embed()
        embed.set_image(url=self._hugs[idx])
        embed.color = int(self._config['COLORS']['info'][1:],16)

        await interaction.send(f"{interaction.user.mention} hugged {user.mention}!",embed=embed)

        return
        
    @nextcord.slash_command(
        name='pat',
        description='Send a pat to a user',
        guild_ids= TESTING_GUILDS
    )
    async def pat(self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(name='user',description='user to pat',required=True)
    ):

        idx = random.randrange(len(self._pats))
        while idx == self._lastPAT:
            idx = random.randrange(len(self._pats))
        self._lastPAT = idx

        embed = nextcord.Embed()
        embed.set_image(url=self._pats[idx])
        embed.color = int(self._config['COLORS']['info'][1:],16)

        await interaction.send(f"{interaction.user.mention} patted {user.mention}!",embed=embed)

        return

    @nextcord.slash_command(
        name='kiss',
        description='Send a kiss to a user',
        guild_ids= TESTING_GUILDS
    )
    async def kiss(self,
        interaction: nextcord.Interaction,
        user: nextcord.Member = nextcord.SlashOption(name='user',description='user to kiss',required=True)
    ):

        idx = random.randrange(len(self._kisses))
        while idx == self._lastKISS:
            idx = random.randrange(len(self._kisses))
        self._lastKISS = idx

        embed = nextcord.Embed()
        embed.set_image(url=self._kisses[idx])
        embed.color = int(self._config['COLORS']['info'][1:],16)

        await interaction.send(f"{interaction.user.mention} kissed {user.mention}!",embed=embed)

        return

    



def setup(bot,**kwargs):
    bot.add_cog(CuteGifs(bot,kwargs))
