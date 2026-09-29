from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">

        <meta name="google-site-verification" content="MUZhxvCmV1ZYtfxHj36Mp7g9P3_tUF0AJlbbeblvQds">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>KIBUTSUJI | Chocolate</title>

        <meta name="description" content="KIBUTSUJI — Chocolate">
        <meta name="robots" content="index, follow">
    </head>

    <body>
        <h1>Chocolate 🍫</h1>
        <p>Welcome to KIBUTSUJI.</p>
        <p>My first website made with Python and Flask.</p>
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=5000)
