from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello! 👋</h1>
    <p>My first website made in Termux!</p>
    """

app.run(host="0.0.0.0", port=5000)
