import sys;
import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;

print("API 2 en Python con VS Code");
print(__name__);
app = flask.Flask(__name__);

class Conexion:
    strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_personas;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def CargarPersonas(self) -> dict:
        respuesta = { };
        try:
            conexion = pyodbc.connect(self.strConnection);
            
            consulta: str = """SELECT * FROM personas""";
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                temporal: dict = { };
                temporal["Id"] = elemento[0];
                temporal["Cedula"] = elemento[1];
                temporal["Nombre"] = elemento[2];
                temporal["Estado"] = elemento[3];
                temporal["Fecha"] = elemento[4];
                temporal["Activo"] = elemento[5];
                respuesta[str(contador)] = temporal;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

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

# http://localhost:4040/main3/CargarPersonas/{}
@app.route('/main3/CargarPersonas/<string:entrada>', methods=["GET"]) # methods=["POST"]
def CargarPersonas(entrada: str) -> str :
    respuesta = { };
    try:
        data = Convertir.ADict(entrada);
        conexion: Conexion = Conexion();
        respuesta["Entidades"] = conexion.CargarPersonas();
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except:
        respuesta["Send"] = sys.exc_info();
        return flask.jsonify(respuesta);

app.run('localhost', 4040);

"""
py -3 --version
py main3.py
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify

py -m pip uninstall Flask
""" 