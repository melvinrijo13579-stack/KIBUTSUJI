from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">

        <meta name="google-site-verification"
              content="MUZhxvCmV1ZYtfxHj36Mp7g9P3_tUF0AJlbbeblvQds">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>KIBUTSUJI</title>

        <style>
            body {
                margin: 0;
                background: black;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            .container {
                margin-top: 120px;
            }

            h1 {
                font-size: 42px;
            }

            button {
                padding: 15px 45px;
                font-size: 20px;
                background: #111;
                color: white;
                border: 2px solid #0066ff;
                border-radius: 10px;
                cursor: pointer;
            }

            #nameBox {
                display: none;
                margin-top: 30px;
            }

            input {
                padding: 13px;
                width: 250px;
                background: #111;
                color: white;
                border: 1px solid #555;
                border-radius: 8px;
                font-size: 16px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Welcome to my first website</h1>

            <button id="startButton">START</button>

            <div id="nameBox">

                <h2>What's your name?</h2>

                <input
                    type="text"
                    id="nameInput"
                    placeholder="Enter your name"
                >

                <br><br>

                <button id="continueButton">
                    Continue
                </button>

            </div>

        </div>


        <script>

            const startButton =
                document.getElementById("startButton");

            const nameBox =
                document.getElementById("nameBox");

            const nameInput =
                document.getElementById("nameInput");

            const continueButton =
                document.getElementById("continueButton");


            startButton.addEventListener("click", function() {

                nameBox.style.display = "block";

                nameInput.focus();

            });


            continueButton.addEventListener("click", function() {

                const name =
                    nameInput.value.trim().toLowerCase();


                if (name === "melvin") {

                    window.location.href = "/melvin";

                }

                else if (name === "abhijit") {

                    window.location.href = "/abhijit";

                }

                else {

                    window.location.href = "/welcome";

                }

            });

        </script>

    </body>
    </html>
    """


@app.route("/melvin")
def melvin():
    return """
    <h1>Melvin's Page</h1>
    <p>This page is ready to be designed.</p>
    """


@app.route("/abhijit")
def abhijit():
    return """
    <h1>Abhijit's Page</h1>
    <p>This page is ready to be designed.</p>
    """


@app.route("/welcome")
def welcome():
    return """
    <h1>Welcome!</h1>
    <p>Your personal KIBUTSUJI page is coming soon.</p>
    """


app.run(host="0.0.0.0", port=5000)
