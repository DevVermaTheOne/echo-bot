from flask import Flask, jsonify,request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route("/bot", methods=["POST", 'GET'])
def response():
    if request.method == 'POST':
        query = dict(request.form)['query']
        res = query + " " + time.ctime()
        return jsonify({"response" : res})
    else:
        return "<h1>You are not suppossed to be here<h1>"
    
if __name__=="__main__":
    app.run(threaded=True, port=5000)