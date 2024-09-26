import sys;
import jsonify;
import flask;
import sys;
import json;
import pyodbc;
import datetime;
import decimal;

print("API en Python con VS Code");
print(__name__);
app = flask.Flask(__name__);

class Estados:
    id: int = 0;
    
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    nombre: str = None;

    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, value: str) -> None:
        self.nombre = value;

class Personas:
    id: int = 0;
    
    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;
        
    cedula: str = None;

    def GetCedula(self) -> str:
        return self.cedula;
    def SetCedula(self, value: str) -> None:
        self.cedula = value;
        
    nombre: str = None;

    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, value: str) -> None:
        self.nombre = value;
        
    estado: int = None;
    
    def GetEstado(self) -> int:
        return self.estado;
    def SetEstado(self, value: int) -> None:
        self.estado = value;
        
    fecha: datetime = None;
    
    def GetFecha(self) -> datetime:
        return self.fecha;
    def SetFecha(self, value: datetime) -> None:
        self.fecha = value;
        
    activo: bool = None;
    
    def GetActivo(self) -> int:
        return self.activo;
    def SetActivo(self, value: int) -> None:
        self.activo = value;
        
    _estado: Estados = None;
    
    def Get_Estado(self) -> Estados:
        return self._estado;
    def Set_Estado(self, value: Estados) -> None:
        self._estado = value;

class Conexion:
    strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_personas;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def CargarPersonas(self) -> None:  
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

class Convert:
    @staticmethod
    def ToDict(data: str) -> dict :
        outcome = { };
        try:
            data = data.replace("'", '"');
            response = json.loads(data);
            return response;
        except:
            print(sys.exc_info());
            return None;

# http://localhost:4040/main3/GetData/{"Send":"Test"}
@app.route('/main3/GetData/<string:income>', methods=["GET"]) # methods=["POST"]
def GetData(income: str) -> str :
    outcome = { };
    try:
        data = Convert.ToDict(income);
        conexion: Conexion = Conexion();
        outcome["Entidades"] = conexion.CargarPersonas();
        outcome["Response"] = "Ok";
        return flask.jsonify(outcome);
    except:
        outcome["Send"] = sys.exc_info();
        return flask.jsonify(outcome);

app.run('localhost', 4040);

"""
py -3 --version
py main3.py
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify

py -m pip uninstall Flask
""" 