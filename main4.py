import sys;
import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;

print("API 3 en Python con VS Code");
print(__name__);
app = flask.Flask(__name__);

class Configuracion:
    strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_personas;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

class PersonasRepositorio:
    def Listar(self, datos: dict) -> dict:  
        conexion = pyodbc.connect(Configuracion.strConnection);
        
        consulta: str = """{CALL proc_select_personas();}""";
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

    def Insertar(self, datos: dict) -> dict:  
        respuesta: dict = { };
        
        conexion = pyodbc.connect(Configuracion.strConnection);
        cursor = conexion.cursor();
        
        cedula: str = datos["Cedula"];
        nombre: str = datos["Nombre"];
        estado: int = datos["Estado"];
        fecha: datetime = datetime.datetime.strptime(datos["Fecha"], "%Y-%m-%d %H:%M:%S");
        activo: bool = datos["Activo"];
        
        consulta: str = "{CALL proc_insert_personas( ";
        consulta += "'" + cedula + "', '" + nombre + "', " + str(estado) + ",";
        consulta += "'" + fecha.strftime("%Y-%m-%d %H:%M:%S") + "', " + str(activo);
        consulta += ", @Resultado);}";
        cursor.execute(consulta);
        
        consulta: str = "SELECT @Resultado;";
        cursor.execute(consulta);
        respuesta["Resultado"] = str(cursor.fetchone()[0]);
        cursor.execute("commit;");

        cursor.close();
        conexion.close();
        return respuesta;

    def Modificar(self, datos: dict) -> dict:  
        respuesta: dict = { };
        
        conexion = pyodbc.connect(Configuracion.strConnection);
        cursor = conexion.cursor();
        
        id: int = datos["Id"];
        cedula: str = datos["Cedula"];
        nombre: str = datos["Nombre"];
        estado: int = datos["Estado"];
        fecha: datetime = datetime.datetime.strptime(datos["Fecha"], "%Y-%m-%d %H:%M:%S");
        activo: bool = datos["Activo"];
        
        consulta: str = "{CALL proc_update_personas( " + str(id) + ", ";
        consulta += "'" + cedula + "', '" + nombre + "', " + str(estado) + ",";
        consulta += "'" + fecha.strftime("%Y-%m-%d %H:%M:%S") + "', " + str(activo);
        consulta += ", @Resultado);}";
        cursor.execute(consulta);
        
        consulta: str = "SELECT @Resultado;";
        cursor.execute(consulta);
        respuesta["Resultado"] = str(cursor.fetchone()[0]);
        cursor.execute("commit;");

        cursor.close();
        conexion.close();
        return respuesta;

    def Borrar(self, datos: dict) -> dict:  
        respuesta: dict = { };
        
        conexion = pyodbc.connect(Configuracion.strConnection);
        cursor = conexion.cursor();
        
        id: int = datos["Id"];
        
        consulta: str = "{CALL proc_delete_personas( " + str(id) + ", @Resultado);}";
        cursor.execute(consulta);
        
        consulta: str = "SELECT @Resultado;";
        cursor.execute(consulta);
        respuesta["Resultado"] = str(cursor.fetchone()[0]);
        cursor.execute("commit;");

        cursor.close();
        conexion.close();
        return respuesta;

class PersonasAplicacion:
    respositorio: PersonasRepositorio = None;

    def __init__(self):
        self.respositorio = PersonasRepositorio();

    def Listar(self, datos: dict) -> None:
        return self.respositorio.Listar(datos);

    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if not "Cedula" in datos.keys() or not "Nombre" in datos.keys() or not "Estado" in datos.keys() or not "Fecha" in datos.keys() or not "Activo" in datos.keys(): 
            respuesta["Error"] = "Falta informacion";
            return respuesta;

        return self.respositorio.Insertar(datos);

    def Modificar(self, datos: dict) -> None:
        respuesta: dict = { };

        if not "Id" in datos.keys() or not "Cedula" in datos.keys() or not "Nombre" in datos.keys() or not "Estado" in datos.keys() or not "Fecha" in datos.keys() or not "Activo" in datos.keys(): 
            respuesta["Error"] = "Falta informacion";
            return respuesta;

        return self.respositorio.Modificar(datos);

    def Borrar(self, datos: dict) -> None:
        respuesta: dict = { };

        if not "Id" in datos.keys(): 
            respuesta["Error"] = "Falta informacion";
            return respuesta;

        return self.respositorio.Borrar(datos);

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

# http://localhost:4040/main4/Listar/{}
@app.route('/main4/Listar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Listar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion = PersonasAplicacion();
        respuesta["Entidades"] = aplicacion.Listar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except:
        respuesta["Send"] = sys.exc_info();
        return flask.jsonify(respuesta);

# http://localhost:4040/main4/Insertar/{"Cedula":"159753", "Nombre": "Test 1", "Estado": "1", "Fecha": "2024-09-28 11:26:08", "Activo": "True"}
@app.route('/main4/Insertar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Insertar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion = PersonasAplicacion();
        respuesta = aplicacion.Insertar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except:
        respuesta["Send"] = sys.exc_info();
        return flask.jsonify(respuesta);

# http://localhost:4040/main4/Modificar/{"Id":"2", "Cedula":"159753", "Nombre": "Test 1", "Estado": "1", "Fecha": "2024-09-28 11:26:08", "Activo": "True"}
@app.route('/main4/Modificar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Modificar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion = PersonasAplicacion();
        respuesta = aplicacion.Modificar(datos);
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except:
        respuesta["Send"] = sys.exc_info();
        return flask.jsonify(respuesta);

# http://localhost:4040/main4/Borrar/{"Id":"2"}
@app.route('/main4/Borrar/<string:entrada>', methods=["GET"]) # methods=["POST"]
def Borrar(entrada: str) -> str :
    respuesta = { };
    try:
        datos = Convertir.ADict(entrada);
        aplicacion: PersonasAplicacion = PersonasAplicacion();
        respuesta = aplicacion.Borrar(datos);
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