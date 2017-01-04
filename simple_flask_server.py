from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/greet", methods=['POST'])
def greet():
    return "Hello " + request.form['text'] + "!"

if __name__ == "__main__":
    app.run(port=5000)