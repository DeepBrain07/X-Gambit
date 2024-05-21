import socket
import json

s = socket.socket()
s.bind(('192.168.1.179', 9999))
s.listen(3)
print("waiting for connections")
playersPos = {}
while True:
    c, address = s.accept()
    player = json.loads(c.recv(1024).decode())
    print(player)
    playersPos[player['id']] = (player['x'], player['y'])
    print(playersPos[player['id']])
    # print("the player's position is ", player)
    c.send(bytes(json.dumps(playersPos), 'utf-8'))
    