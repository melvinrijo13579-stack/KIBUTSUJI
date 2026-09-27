from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Website</title>
    </head>

    <body>
        <h1>Eline ❤️ Melvin</h1>
        <p>yes it is you website melvin this is working keep going she may not love yiu but dont stp loving her.</p>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)
