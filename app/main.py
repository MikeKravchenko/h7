import socket
from hl7apy.parser import parse_message
from flask import Flask, request, abort
app = Flask(__name__)

HOST = 'localhost'
PORT = 6789

@app.route("/savedata")
def h7query():
    name = request.args.get("name")
    surname = request.args.get("surname")
    
    message = f"name: {name}, age: {surname}"
    print(f"Got: {message}")
    if name is None or surname is None:
        print("Wrong params, terminated")
        abort(400, "Wrong input")

    res = query(name, surname)
    if repr(res):
        return "OK"
    else:
        abort(400, "HL7 parse error") 

# route poluchit parametru uzera
# parametry -> funk quire
# paremertu messege

def query(name, surname):
    msg = \
        'MSH|^~\&|REC APP|REC FAC|SEND APP|SEND FAC|20110708163513||QBP^Q22^QBP_Q21|111069|D|2.5|||||ITA||EN\r' \
        f'QPD|IHE PDQ Query|111069|@PID.5.2^{name}|@PID.5.1.1^{surname}|||\r' \
        'RCP|I|'
    # establish the connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
        # send the message
        sock.sendall(parse_message(msg).to_mllp().encode('UTF-8'))
        # receive the answer
        received = sock.recv(1024*1024)
        return received
    finally:
        sock.close()


if __name__ == '__main__':
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)