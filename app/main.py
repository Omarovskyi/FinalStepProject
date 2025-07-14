from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def get_host_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"<strong>Host IP: </strong>{ip}\n"
