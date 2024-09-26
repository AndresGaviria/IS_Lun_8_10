import sys;
import jsonify;
import flask;
import sys;
import json;
import datetime;

print("API en Python con VS Code");
print(__name__);
app = flask.Flask(__name__);

class Convert:
    @staticmethod
    def ToDict(data: str) -> dict :
        outcome = { };
        try:
            data = data.replace("'", '"');
            response = json.loads(data);
            return response;
        except:
            print(sys.exc_info());
            return None;

# http://localhost:4040/main2/GetData/{"Send":"Test"}
@app.route('/main2/GetData/<string:income>', methods=["GET"]) # methods=["POST"]
def GetData(income: str) -> str :
    outcome = { };
    try:
        data = Convert.ToDict(income);
        outcome["Send"] = data["Send"];
        outcome["Response"] = datetime.datetime.now();
        return flask.jsonify(outcome);
    except:
        outcome["Send"] = sys.exc_info();
        return flask.jsonify(outcome);

app.run('localhost', 4040);

"""
py -3 --version
py main2.py
py -m pip install pyodbc
py -m pip install Flask
py -m pip install jsonify

py -m pip uninstall Flask
""" 