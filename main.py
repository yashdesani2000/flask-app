from re import T
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('dhaval.html')


app.run(debug=True)
