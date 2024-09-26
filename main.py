import pyodbc;
import datetime;
import decimal;

"""
  varInteger: int = 253; # int(253)
  varLong: int = 2350006657; # int(2350006657)
  varDouble: float = 10.2; # float(10.2)
  varDecimal: decimal = 10.2; # Decimal(10.2)
  varComplex: complex = 10.2; # complex(10.2)
  varString: str = "Sammy Canela"; # str("Sammy Canela")
  varDate: datetime = datetime.datetime.now();
  varBool: bool = True; # bool(True)
"""

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

    def ConexionBasica(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        
        consulta: str = """SELECT * FROM personas""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        for elemento in cursor:
            print(elemento);
            
        cursor.close();
        conexion.close();

    def ConexionBasica1(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        
        consulta: str = """SELECT * FROM estados""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
          entidad = Estados();
          entidad.SetId(elemento[0]);
          entidad.SetNombre(elemento[1]);
          lista.append(entidad);
            
        cursor.close();
        conexion.close();

        for estado in lista:
            print(str(estado.GetId()) + " - " + estado.GetNombre());

    def ConexionBasica2(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        
        consulta: str = """
          SELECT p.id, 
                p.cedula, 
                p.nombre, 
                p.estado, 
                p.fecha, 
                p.activo, 
                e.id, 
                e.nombre
          FROM estados e
            INNER JOIN personas p ON e.id = p.estado""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
          entidad = Personas();
          entidad.SetId(elemento[0]);
          entidad.SetCedula(elemento[1]);
          entidad.SetNombre(elemento[2]);
          entidad.SetEstado(elemento[3]);
          entidad.SetFecha(elemento[4]);
          entidad.SetActivo(elemento[5]);

          estado = Estados();
          estado.SetId(elemento[6]);
          estado.SetNombre(elemento[7]);
          entidad.Set_Estado(estado);
          
          lista.append(entidad);
            
        cursor.close();
        conexion.close();

        for estado in lista:
            print(str(estado.GetId()) + " - " + 
              estado.GetCedula() + " - " + 
              estado.GetNombre() + " - " + 
              estado.Get_Estado().GetNombre() + " - " + 
              str(estado.GetEstado()) + " - " + 
              str(estado.GetFecha()) + " - " + 
              str(estado.GetActivo()));

    def NonQueryBasico(self) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();

        cedula: str = "7532564";
        nombre: str = "Test Python";
        estado: int = 3;
        fecha: datetime = datetime.datetime.now();
        activo: bool = True;

        consulta: str = "INSERT INTO `personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) ";
        consulta += "VALUES ('" + cedula + "', '" + nombre + "', " + str(estado) + ",";
        consulta += "'" + fecha.strftime("%Y-%m-%d %H:%M:%S") + "', " + str(activo) + ")";

        cursor.execute(consulta);
        cursor.execute("SELECT LAST_INSERT_ID()");
        cursor.commit();       
                
        print("Response Inserted Objects: " + str(cursor.fetchone()[0]));
        cursor.close();
        conexion.close();

    def ConexionProcedimiento(self) -> None:  
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();
        
        consulta: str = """{CALL proc_select_estados();}""";
        cursor.execute(consulta);

        for elemento in cursor:
            print(elemento);
            
        cursor.close();
        conexion.close();

    def ProcedimientoConSalida(self) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();

        nombre: str = "Estado 32";

        consulta: str = "{CALL proc_insert_estados('" + nombre + "', @Resultado);}";
        cursor.execute(consulta);
        # consulta: str = "{CALL proc_insert_estados(?, @Resultado);}";
        # cursor.execute(consulta, (nombre));

        consulta: str = "SELECT @Resultado;";
        cursor.execute(consulta);
        print("Response Inserted Objects: " + str(cursor.fetchone()[0]));
        cursor.execute("commit;");

        cursor.close();
        conexion.close();

    def ProcedimientoInsert(self) -> None:
        conexion = pyodbc.connect(self.strConnection);
        cursor = conexion.cursor();

        cedula: str = "4532569";
        nombre: str = "Test Python 3";
        estado: int = 1;
        fecha: datetime = datetime.datetime.now();
        activo: bool = True;

        consulta: str = "{CALL proc_insert_personas( ";
        consulta += "'" + cedula + "', '" + nombre + "', " + str(estado) + ",";
        consulta += "'" + fecha.strftime("%Y-%m-%d %H:%M:%S") + "', " + str(activo);
        consulta += ", @Resultado);}";
        cursor.execute(consulta);

        consulta: str = "SELECT @Resultado;";
        cursor.execute(consulta);
        print("Response Inserted Objects: " + str(cursor.fetchone()[0]));
        cursor.execute("commit;");    
                
        cursor.close();
        conexion.close();

print("Conexion en Python con VS Code");
conexion: Conexion = Conexion();
# conexion.NonQueryBasico();
# conexion.ConexionBasica();
# conexion.ConexionBasica1();
# conexion.ConexionProcedimiento();
# conexion.ProcedimientoConSalida();
# conexion.ConexionProcedimiento();
conexion.ProcedimientoInsert();
conexion.ConexionBasica2();

"""
py -3 --version
py main.py
py -m pip install pyodbc

""" 