import jwt
import hashlib
import binascii, os
from Crypto.Cipher import AES
from Nucleo import Test;

# No utlizarlo al dia de hoy
class EncriptarMD5:
    def Executar(self) -> None :
        valor = "Test";
        print("Value: " + valor);
        resutlado = self.Encriptar(valor);
        print("Encrypt: " + resutlado);

        valor = "TEst";
        print("Value: " + valor);
        resutlado = self.Encriptar(valor);
        print("Encrypt: " + resutlado);

        valor = "gjghdhjw767876987d";
        print("Value: " + valor);
        resutlado = self.Encriptar(valor);
        print("Encrypt: " + resutlado);
        
    def Encriptar(self, valor: str) -> str :
        return str(hashlib.md5(valor.encode('utf-8')).hexdigest());

    def Descifrar(self, valor: str) -> str :
        return None;

class EncriptarAES1:
    secretKey = os.urandom(32);

    def Executar(self) -> None :
        valor = "Test";
        print("Value: " + valor);
        resultado = self.Encriptar(valor);
        print("Encrypt: " + binascii.hexlify(resultado[0]).decode());

        resultado = self.Descifrar(resultado);
        print("Decrypt: " + resultado.decode());

        valor = "Test skhdjgfsad7 v79374679 adjsgfkjasd 79qw46 87asd hgfhj";
        print("Value: " + valor);
        resultado = self.Encriptar(valor);
        print("Encrypt: " + binascii.hexlify(resultado[0]).decode());

        resultado = self.Descifrar(resultado);
        print("Decrypt: " + resultado.decode());
        
    def Encriptar(self, valor: str) -> str :
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        return (ciphertext, aesCipher.nonce, authTag);

    def Descifrar(self, valor: str) -> str :
        (ciphertext, nonce, authTag) = valor;
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext;

print("ENCRIPT 4 Python con VS Code");
print("MD5---------------------------");
test = EncriptarMD5();
test.Executar();

print("AES---------------------------");
test = EncriptarAES1();
test.Executar();


print("JWT---------------------------");
try:
    key = "KJhisdy878779ghdfgh45645634564356";

    # Generar el codigo de autenticacion
    encoded = jwt.encode({"Usuario": "Pepito"}, key, algorithm="HS256");
    print(encoded);

    # Genera un error al no ser una clave correcta
    # encoded = "Test"; 
    # encoded = "12345678901sdjgfjshNiIsInR5cCI6IkpXVCJ9.eyJVc3VhcmlvIjoiUGVwaXRvUGVyZXoifQ.wX5VYb2e7HxtBuReObp0SULKzEqs_eDC7aqFc3dxoRE";
    resultado = jwt.decode(encoded, key, algorithms="HS256");
    print(resultado["Usuario"]);
except Exception as ex:
    print(ex);


test = Test.Test();
print(test.Ejecutar());

"""
    ** Sin base de proyecto para modificar no hay nota!
    ** El usuario lo pueden quemar en un archivo .py, no tiene que ir a base datos u otra cosa, para el JWT
    ** Los servicios deben tener Capa de Repositorio, Aplicacion, Servicio 
    (Indiviudales, Excepcion Servicio: puede ser uno solo)
    ** Todos con commit en el GIT, necesitamos 2 repositorios o Ramas

    py -m pip install pycryptodome
    py -m pip install PyJWT

    * Para las tablas -- Esto es opcional si deciden usar AES_ENCRYPT o el cifrado en 
    base de datos
    SELECT AES_ENCRYPT('Test', 'ytuysy76887');
    SELECT AES_DECRYPT(AES_ENCRYPT('Test', 'ytuysy76887'), 'ytuysy76887');

        `name` blob NOT NULL,
"""