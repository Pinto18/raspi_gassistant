#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    content = jsonify({'command' : 'sudo shutdown -h now'})
    return content, 200 

@app.route('/reboot', methods=['GET'])
def reboot():
    content = jsonify({'command' : 'sudo reboot'}) 
    return content, 200

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
