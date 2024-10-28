import pyodbc;
import datetime;
import decimal;
from Utilidades import Configuracion; 

class PersonasRepositorio:
    def Listar(self, datos: dict) -> dict:  
        respuesta = { };
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);
            
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
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

    def Insertar(self, datos: dict) -> dict: 
        respuesta: dict = { };
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);
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
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

    def Modificar(self, datos: dict) -> dict: 
        respuesta: dict = { };
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);
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
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

    def Borrar(self, datos: dict) -> dict:  
        respuesta: dict = { };
        try:
            conexion = pyodbc.connect(Configuracion.Configuracion.strConnection);
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
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;