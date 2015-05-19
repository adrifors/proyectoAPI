from twitterAPI import *


def getTweetsSearch(busqueda):
    twitter_api =  oauth_login()
    localizacion = "40.2085,-3.713,497mi"
    tweets = twitter_api.search.tweets(q=busqueda, count=1000, geocode=localizacion)
    #aux = json.dumps(tweets, indent = 1)
    resultado = []
    for tweet in tweets['statuses']:
        resultado.append(tweet['text'])
    return resultado

#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()

