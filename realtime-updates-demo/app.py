from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('echo')
def echo(data):
    try:
        while True:
            data = data['message']
            socketio.emit('echo_response', {'message': data})

    except Exception as err:
        print("DATA ERRORED", data)


if __name__ == "__main__":
    socketio.run(app, debug=True)
