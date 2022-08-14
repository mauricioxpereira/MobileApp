'''
pip install "python-socketio[client]"
pip install "python-socketio[asyncio_client]"
'''
import socketio
from time import sleep # just used for timing the messages

sio = socketio.Client()

@sio.event
def connect():
    print('Connection established with server to send message data.')

def send_msg(msg):
    print("sending")
    sio.emit('msg', msg)

@sio.event
def disconnect():
    print('Disconnected from websocket! Cannot send message data.')

sio.connect('ws://localhost:3000')

# Example of list of messages to send
MESSAGE_LIST = ["66903222854465",
                "36558352171508",
                "42493680134299",
                "32010903761366",
                "37556732408598",
                "00418984412935",
                "54555467232969",
                "95461295964563",
                "63543734057786",
                "37925062203941"]

# logic to send the 10 messages then close connection
x = 0
while x < 10:
    send_msg(MESSAGE_LIST[x])
    sleep(1)
    x += 1

sio.disconnect()