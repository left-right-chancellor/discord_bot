from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<!DOCTYPE html><html><head><meta charset="utf-8" /><title>男娘機機</title><style>body{background:#202020;color:#fff;font-family:monospace;}</style></head><body>機機> python3 mian.py<br />Operating. </body></html>'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()