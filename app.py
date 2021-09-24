from flask import Flask, Response
import os
from subprocess import call
from werkzeug.exceptions import ExpectationFailed
app = Flask(__name__)

@app.route('/startapp', methods=['POST'])    
def runapp():
    try:
        # os.system('/bin/bash -c cd /home/orgacac/develop/nexmo-voice-interface-asr && node app-gstt.js')
        os.system('/bin/bash -c runapp.sh')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

@app.route('/stopapp', methods= ["POST"])
def killapp():
    try:
        os.system('kill $(lsof -t -i:3000)')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

@app.route('/startbot', methods =["POST"])
def botrun():
    try:
        # os.system('/bin/bash -c source /home/orgacac/develop/botenv/bin/activate && cd /home/orgacac/develop/cpf_nomination_bot && rasa run --enable-api -p 500')
        os.system('/bin/bash -c runbot.sh')
        res = Response(status=200)
    except TypeError as err:
        res = err
    print(res)
    return res

@app.route('/stopbot', methods= ["POST"])
def killbot():
    try:
        os.system('kill $(lsof -t -i:5005)')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)