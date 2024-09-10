import pyodbc;
import datetime;
import decimal;

print("Hola mundo");

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
    id: int;

    def GetId(self) -> int: 
        return self.id;
    def SetId(self, valor: int) -> None: 
        self.id = valor;

    nombre: str;

    def GetNombre(self) -> str: 
        return self.nombre;
    def SetNombre(self, valor: str) -> None: 
        self.nombre = valor;

class Conexion:
    string_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_personas;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

    def ConnectionBasica(self) -> None:  
        conexion = pyodbc.connect(self.string_conexion);
        
        consulta: str = """SELECT * FROM estados""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        for elemento in cursor:
            print(elemento);

        conexion.close();

    def ConnectionPersonas(self) -> None:  
        conexion = pyodbc.connect(self.string_conexion);
        
        consulta: str = """
            SELECT p.id,
                p.cedula,
                p.nombre,
                p.estado,
                p.fecha,
                p.activo,
                e.id,
                e.nombre
            FROM personas p 
                INNER JOIN estados e ON p.estado = e.id""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        for elemento in cursor:
            print(elemento);

        conexion.close();

    def ConnectionBasicaTipo(self) -> None:  
        conexion = pyodbc.connect(self.string_conexion);
        
        consulta: str = """SELECT * FROM estados""";
        cursor = conexion.cursor();
        cursor.execute(consulta);

        lista: list = [];
        for elemento in cursor:
            estado: Estados = Estados();
            estado.SetId(elemento[0]);
            estado.SetNombre(elemento[1]);
            lista.append(estado);

        conexion.close();

        for estado in lista:
            print(str(estado.GetId()) + " - " + estado.GetNombre());

    
    def ConnectionNonQuery(self) -> None:  
        conexion = pyodbc.connect(self.string_conexion);
        cursor = conexion.cursor();
        
        nombre: str = "Python estado";

        consulta: str = "INSERT INTO `estados` (`nombre`) VALUES ('" + nombre + "')";
        cursor.execute(consulta);
        cursor.execute("SELECT LAST_INSERT_ID()");
        cursor.commit();  

        print("Filas afectadas: " + str(cursor.fetchone()[0]));
        cursor.close();
        conexion.close();

conexion: Conexion = Conexion();
# conexion.ConnectionBasica();
conexion.ConnectionNonQuery();
conexion.ConnectionBasicaTipo();

estado: Estados = Estados();
estado.SetId(0);
estado.SetNombre("Test");