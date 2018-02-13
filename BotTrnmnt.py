import discord
from discord.ext import commands
import json
import requests

class BotTrnmnt:
    """My bot that gets open tournaments for Clash Royale Players!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def torneiosgratis():
        # encoding=utf8
        import sys
        reload(sys)
        sys.setdefaultencoding('utf8')

        url = "http://statsroyale.com/tournaments?appjson=1"
        response = requests.get(url)

        torneiosDict=json.loads(response.text)

        for torneio in torneiosDict['tournaments']:
            jaComecou=torneio['warmupOver']
            bloqueado=torneio['locked']
            inscritos=torneio['totalPlayers']
            limite=torneio['maxPlayers']
            tempoEmFalta=torneio['timeLeft']
            m, s = divmod(tempoEmFalta, 60)
            h, m = divmod(m, 60)
            if (jaComecou==0 and bloqueado==False and inscritos != limite) :
                await self.bot.say( ' ----------------- ')
                await self.bot.say( 'Titulo -  ' + torneio['title'])
                await self.bot.say( 'Descricao - ' + torneio['description'])
                await self.bot.say( 'Tag do torneio - #' + str(torneio['hashtag']))
                await self.bot.say( 'Jogadores inscritos - ' + str(inscritos))
                await self.bot.say( 'Limite de jogadores - ' + str(limite))    
                await self.bot.say( 'Tempo para comecar - ' + str(torneio['warmup']))
                await self.bot.say( 'Começa daqui a ' + "%d:%02d:%02d" % (h, m, s) + ' horas')
        
        if (len(torneiosDict)==0):
            await self.bot.say( 'Nao ha torneios gratuitos neste instante... :(')

        await self.bot.say( 'O eunito manda cumprimentos! :)'
                           
def setup(bot):
    bot.add_cog(BotTrnmnt(bot))
