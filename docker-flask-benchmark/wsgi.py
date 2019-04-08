# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Python!"

if __name__ == '__main__':
    app.run()
