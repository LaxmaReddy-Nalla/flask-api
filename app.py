from flask import Flask, Response
import os
from subprocess import call
from werkzeug.exceptions import ExpectationFailed
app = Flask(__name__)

@app.route('/data', methods=["GET"])
def home():
    os.system('ls -al')
    return 'HOME PAGE'
@app.route('/runapp', methods=['POST'])    
def runapp():
    try:
        os.system('cd /home/orgacac/develop/nexmo-voice-interface-asr && node app-gstt.js')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

@app.route('/killapp', methods= ["POST"])
def killapp():
    try:
        os.system('kill $(lsof -t -i:3000)')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

@app.route('/runbot', methods =["POST"])
def botrun():
    try:
        os.system('/bin/bash -c ./script.sh')
        res = Response(status=200)
    except TypeError as err:
        res = err
    print(res)
    return res

@app.route('/killbot', methods= ["POST"])
def killbot():
    try:
        os.system('kill $(lsof -t -i:5005)')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

if __name__ == "__main__":
    app.run(debug=True)