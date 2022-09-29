from cProfile import run
# Importovaný modul flask dělá server. 
from flask import Flask

app = Flask(__name__)

#První odpověď servru byla věta Hello, World!
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#druhá odpověď servru s dodatkem adresy /whatever byla "ahoj, jak se máš"
@app.route("/whatever")
def whatever():
    my_string = "ahoj, jak se mas"

    return my_string

# flask --app main.py run v první konzoli spustil server
