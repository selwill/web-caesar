from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

page_body = """
<!DOCTYPE html>
<html>
<style>
form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
    <body background="https://drive.google.com/uc?id=1q8O7pIYBXas8Jwwgx6yteDSZfu3BTgvG" style ="width:70%;">
        <h1>Hello world!</h1>
        <p><a href="https://www.w3schools.com">Visit W3Schools.com!</a></p>
    </body>
</html>
"""
caesar_form = """
    <form action="/casesar-it" method="post">

        <input type="text" name-"rot" label="Encrypt It">
        
        <textarea name="text" name="text" value=0>
    </form>
"""


@app.route("/")
def index():
    content = page_body

    return content

app.run()