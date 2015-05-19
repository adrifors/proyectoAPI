from twitterAPI import *
from flask import Flask, render_template
from flask import request, jsonify
from utilidades import *
from dropAPI import *

app = Flask(__name__)


twitter_api =  oauth_login()

#Para guardar el fichero con todos los datos de los tweets que coinciden con la busqueda
@app.route("/dropsave", methods=['POST'])
def dropsave() :
    client = loginDropbox()
    query = request.form['text']
    OUT_FILE = query
    tweets = getTweetsSearch(query)
    aux = json.dumps(tweets, indent = 1)
    save_json(OUT_FILE, aux)
    response = put(client, OUT_FILE)
    return jsonify({'result': True})

#despliegue 1 del menu
@app.route("/search")
def search():
    return render_template('buscar.html')

#despliegue 2 del menu
@app.route("/save")
def save():
    return render_template('guardar.html')

#Busqueda de tweets con un query determinado
@app.route("/buscar", methods=['POST'])
def buscar():
    query = request.form['text']
    tweets = getTweetsSearch(query)
    return json.dumps(tweets, indent = 1)

#TRENDS de Spain
@app.route("/ttspain")
def ttspain():
    SPAIN_WOE_ID =  23424950
    spain_trends = twitter_api.trends.place(_id=SPAIN_WOE_ID)

    consultas = [ status['query'] for status in spain_trends[0]['trends'] ]
    return json.dumps(consultas, indent = 1)
    
#Raiz de la app
@app.route("/")
def index():
	return render_template('menu.html')


if __name__ == "__main__":
    app.run(debug=True)
