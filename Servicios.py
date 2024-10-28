import sys;
import jsonify;
import flask;
import json;
import datetime;
import decimal;
from Aplicaciones import PersonasAplicacion;
from Utilidades import Configuracion, Convertir;

print(__name__);
app = flask.Flask(__name__);

# http://localhost:4040/Servicios/Listar/{}
@app.route('/Servicios/Listar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Listar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion.PersonasAplicacion = PersonasAplicacion.PersonasAplicacion();
        respuesta["Entidades"] = aplicacion.Listar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return flask.jsonify(respuesta);

# http://localhost:4040/Servicios/Insertar/{"Cedula":"159753", "Nombre": "Test 1", "Estado": "1", "Fecha": "2024-09-28 11:26:08", "Activo": "True"}
@app.route('/Servicios/Insertar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Insertar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion.PersonasAplicacion = PersonasAplicacion.PersonasAplicacion();
        respuesta = aplicacion.Insertar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return flask.jsonify(respuesta);

# http://localhost:4040/Servicios/Modificar/{"Id":"2", "Cedula":"159753", "Nombre": "Test 1", "Estado": "1", "Fecha": "2024-09-28 11:26:08", "Activo": "True"}
@app.route('/Servicios/Modificar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Modificar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion.PersonasAplicacion = PersonasAplicacion.PersonasAplicacion();
        respuesta = aplicacion.Modificar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return flask.jsonify(respuesta);

# http://localhost:4040/Servicios/Borrar/{"Id":"2"}
@app.route('/Servicios/Borrar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Borrar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion.PersonasAplicacion = PersonasAplicacion.PersonasAplicacion();
        respuesta = aplicacion.Borrar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return flask.jsonify(respuesta);

app.run('localhost', 4040);

"""
py -3 --version
py Servicios.py

http://localhost:4040/Servicios/Listar/{}
http://localhost:4040/Servicios/Insertar/{'Activo':true, 'Cedula':'1242342', 'Estado':1,'Nombre':'Pruebas', 'Fecha':'2024-10-28 11:28:38'}
http://localhost:4040/Servicios/Modificar/{'Activo':true, 'Cedula':'1242342', 'Estado':1,'Nombre':'Test 123', 'Fecha':'2024-10-28 11:28:38', 'Id':3}
http://localhost:4040/Servicios/Borrar/{'Activo':true, 'Cedula':'1242342', 'Estado':1,'Nombre':'Test 123', 'Fecha':'2024-10-28 11:28:38', 'Id':3}
""" 