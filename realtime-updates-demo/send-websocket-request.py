import socketio

# Create a SocketIO client instance
sio = socketio.Client()

# Connect to the Flask-SocketIO server
sio.connect('http://127.0.0.1:5000')

# Define a function to send WebSocket requests
def send_websocket_request(message):
    sio.emit('echo', {'message': message})

# Define a callback function to handle responses from the server
@sio.on('echo_response')
def handle_echo_response(data):
    print(f'Received from server: {data["message"]}')

if __name__ == '__main__':
    while True:
        message = input('Enter a message to send (or "exit" to quit): ')
        if message.lower() == 'exit':
            break
        send_websocket_request(message)

    sio.disconnect()
