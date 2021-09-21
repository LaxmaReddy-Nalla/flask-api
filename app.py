from flask import Flask, Response
import os
from subprocess import call
from werkzeug.exceptions import ExpectationFailed
app = Flask(__name__)

@app.route('/data', methods=["GET"])
def home():
    os.system('ls -al')
    return 'HOME PAGE'
@app.route('/runapp', methods=['GET'])    
def runapp():
    try:
        os.system('node /home/laxmareddy/ACAC/nexmo-asr/app-gstt.js &')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

@app.route('/killapp', methods= ["GET"])
def killapp():
    try:
        os.system('kill $(lsof -t -i:3000)')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

@app.route('/runbot', methods =["GET"])
def botrun():
    try:
        os.system('/bin/bash -c ./script.sh')
        res = Response(status=200)
    except TypeError as err:
        res = err
    print(res)
    return res

@app.route('/killbot', methods= ["GET"])
def killbot():
    try:
        os.system('kill $(lsof -t -i:5005)')
        res = Response(status=200)
    except TypeError as err:
        res = err
    return res

if __name__ == "__main__":
    app.run(debug=True)