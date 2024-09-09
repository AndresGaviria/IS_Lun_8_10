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

conexion: Conexion = Conexion();
conexion.ConnectionBasica();