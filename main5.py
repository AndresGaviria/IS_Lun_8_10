import hashlib
import binascii, os
from Crypto.Cipher import AES

class EncriptarMD5:
    def Executar(self) -> None :
        valor = "Test";
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

"""
py -3 --version
py main5.py
py -m pip install pycryptodome

py -m pip uninstall pycryptodome
""" 