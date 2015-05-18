# -*- coding: utf-8 -*-

import dropbox

#Funcion para loguearnos en Dropbox
def loginDropbox() :
    #Claves de la API de Dropbox
    app_key = 'ovdru3winthm2dd'
    app_secret = 'luwbxz035kdt2qs'

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

    #Generamos la url de la que tendremos que obtener la clave de autorizacion
    authorize_url = flow.start()

    #Mediante la terminal tendremos que seguir los pasos e intrudocir el codigo de autorizacion
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()

    #Si el codigo es incorrecto esto dara error
    access_token, user_id = flow.finish(code)

    client = dropbox.client.DropboxClient(access_token)
    return client

#Funcion para guardar el fichero generado con la busqueda en dropbox
def put(client, fichero) :
    aux=fichero+".json"
    f = open(aux, 'rb')
    response = client.put_file( aux, f)
    return response
