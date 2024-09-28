import sys;
import jsonify;
import flask;
import sys;
import json;
import datetime;

print("API 1 en Python con VS Code");
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

"""
py -3 --version
py main2.py
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify

py -m pip uninstall Flask
""" 