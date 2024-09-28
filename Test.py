import pyodbc;
import datetime;
import decimal;

fecha: datetime = datetime.datetime.now();
print(fecha.strftime("%Y-%m-%d %H:%M:%S"));