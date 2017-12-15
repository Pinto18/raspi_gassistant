#!flask/bin/python
from flask import Flask, jsonify
from flask.ext.api import status

app = Flask(__name__)

@app.route('/shutdown')
def shutdown():
    content = jsonify({'command' : 'sudo shutdown -h now'})
    return content, status.HTTP_200_OK 

@app.route('/reboot')
def reboot():
    content = jsonify({'command' : 'sudo reboot'}) 
    return content, status.HTTP_200_OK 

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
