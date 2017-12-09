#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/shutdown')
def shutdown():
    return jsonify({'command':'sudo shutdown -h now'})

@app.route('/reboot')
def reboot():
    return jsonify({'command':'sudo reboot'})

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)