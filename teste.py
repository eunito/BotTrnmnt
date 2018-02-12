# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import requests
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
        print ' ----------------- '
        print 'Titulo -  ' + torneio['title']
        print 'Descricao - ' + torneio['description']
        print 'Tag do torneio - #' + str(torneio['hashtag'])
        print 'Jogadores inscritos - ' + str(inscritos)
        print 'Limite de jogadores - ' + str(limite)
        print 'Começa daqui a ' + "%d:%02d:%02d" % (h, m, s) + ' horas'

if (len(torneiosDict)==0):
    print 'Nao ha torneios gratuitos neste instante... :('

