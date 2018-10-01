from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <style>
        form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
        }}
        textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
        }}
        img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
        }}
    </style>
    <body background="https://drive.google.com/uc?id=1q8O7pIYBXas8Jwwgx6yteDSZfu3BTgvG" style ="width:70%;">
        
        <form method="POST">
            <label>Rotate by</label>
            <input type="text" name="rot" value=0 />
        
            <textarea name="text" name="text" />{0} </textarea>

            <input type="submit" value="Encrypt It" />
        </form>


    </body>
</html>
"""

@app.route("/")
def index():
    
    return form.format('')


@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    rot = int(rot)
    words = rotate_string(text, rot)

    return form.format(rotate_string(words, rot))

app.run()