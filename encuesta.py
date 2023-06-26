#PROGRAMA PRINCIPAL - ENCUESTA


from contextlib import nullcontext


import os
from flask import Flask, send_from_directory, redirect, url_for ,render_template, request
from werkzeug.utils import secure_filename

from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
import pymongo



app = Flask(__name__)

CONNECTION_STRING ="mongodb+srv://catdog-23:Admin_8723@cluster0.wf7ii.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)

db = client.Encuesta

coleccion = db.Respuestas


#app.config['UPLOAD_FOLDER'] = 'static/images'
#ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


no_encuesta = 0
encuestas = {}



@app.route("/")
def home():
    return render_template("base.html")


@app.route('/encuesta', methods = ['POST', 'GET'])
def encuesta():
    
    if request.method == 'POST':
        
        plataforma = request.form['plataforma']
        contenido = request.form['contenido']
        genero = request.form['genero']
        videoseducativos = request.form['videoseducativos']
        duracion = request.form['duracion']
        nombre = request.form['nombre']
       
        """
        ESTA PARTE DEL CÓDIGO ES PARA SUBIR IMÁGENES AL SERVIDOR
        file = request.files['archivo']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        filename = 'images/' + filename
        """

        global no_encuesta
        no_encuesta += 1
        id_encuesta = (str(no_encuesta))
        nueva_encuesta = {
            
           
            "plataforma" : plataforma,
            "contenido" : contenido,
            "genero" : genero,
            "videoseducativos" : videoseducativos,
            "duracion" : duracion,
            "nombre" : nombre
            
        }

        encuestas.update({id_encuesta : nueva_encuesta})

       
        coleccion.insert_one(nueva_encuesta)
        
        #datos = (nombre, raza, sexo, caracter, color, edad, tamanio, salud, sociable, contacto, filename)
        #return redirect(url_for("lista", data=datos))
        print(encuestas)
        return resultados(data=encuestas)
        
        
    
    else:
        pass
        return render_template("encuesta.html")
     

@app.route('/resultados', methods = ['POST', 'GET'])
def resultados(data={}):
    
    print(data)
    return render_template("resultados.html", dic = data)
    
    
    
if __name__ == '__main__':   
    app.run(threaded= True, debug = True) 
    




