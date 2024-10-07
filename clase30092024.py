import sys;
import jsonify;
import flask;
import json;
import datetime;

print("Clase del 30-09-2024");
print(__name__);
app = flask.Flask(__name__);

class Convertir:
    @staticmethod
    def ADict(data: str) -> dict :
        respuesta = { };
        try:
            data = data.replace("'", '"');
            respuesta = json.loads(data);
            return respuesta;
        except:
            print(sys.exc_info());
            return None;

diccionario = Convertir.ADict("{'Id':'1', 'Cedula':'76782687'}");
print(diccionario["Id"]);
print(diccionario["Cedula"]);

# http://localhost:4040/main2/ObtenerDatos/{"Send":"Test"}
@app.route('/main2/ObtenerDatos/<string:entrada>', methods=["GET"]) # methods=["POST"]
def ObtenerDatos(entrada: str) -> str :
    respuesta = { };
    try:
        data = Convertir.ADict(entrada);
        respuesta["Send"] = data["Send"];
        respuesta["Response"] = datetime.datetime.now();
        return flask.jsonify(respuesta);
    except:
        respuesta["Send"] = sys.exc_info();
        return flask.jsonify(respuesta);

app.run('localhost', 4040);