from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

page_body = """
<!DOCTYPE html>
<html>
<style>
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

@app.route("/")
def index():
    content = page_body

    return content

app.run()