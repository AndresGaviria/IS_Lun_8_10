import datetime;
import decimal;
from Repositorios import PersonasRepositorio;

class PersonasAplicacion:
    respositorio: PersonasRepositorio.PersonasRepositorio = None;

    def __init__(self):
        self.respositorio = PersonasRepositorio.PersonasRepositorio();

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