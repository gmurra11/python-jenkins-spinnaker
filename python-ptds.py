from flask import Flask, flash, redirect, render_template, request, session, abort
from prometheus_flask_exporter import PrometheusMetrics
import socket

app = Flask(__name__)
metrics = PrometheusMetrics(app)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
version = open('version.txt').read().strip()

data=open("/etc/resolv.conf", 'r')
for line in data.readlines():
   if 'search' in line:
      namespace = line.split()[1];

@app.route("/")
def getRoute():
    return render_template('index.html');

@app.route("/ptds/")
def getApp():
    return render_template('form.html', ip=ip, hostname=hostname, version=version, namespace=namespace);

if __name__ == "__main__":
    app.run(host="0.0.0.0")
