import sys;
import json;

class Convertir:
    @staticmethod
    def ADict(data: str) -> dict :
        respuesta = { };
        try:
            data = data.replace("'", '"');
            respuesta = json.loads(data);
            return respuesta;
        except:
            print(sys.exc_info());
            return None;