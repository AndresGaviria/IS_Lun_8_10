import jwt

try:
    key = "KJhisdy8787798udfsd56f4s5d4fsdf";

    # Generar el codigo de autenticacion
    encoded = jwt.encode({"Usuario": "Test.khdg7826387"}, key, algorithm="HS256");
    print(encoded);

    # Genera un error al no ser una clave correcta
    # encoded = "Test"; 
    # encoded = "123567890JIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc3VhcmlvIjoiVGVzdC5raGRnNzgyNjM4NyJ9.NGiyqE1ACa0sQ9Ps1ETmyP-KwxufiyW9hK0HImik6Dw";
    resultado = jwt.decode(encoded, key, algorithms="HS256");
    print(resultado["Usuario"]);
except Exception as ex:
    print(ex);

"""
py -3 --version
py main6.py
py -m pip install PyJWT

py -m pip uninstall PyJWT
""" 