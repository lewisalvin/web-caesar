from flask import Flask, request
from caesar import rotate_string
app= Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
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
        </style>
    </head>
    <body>
      <form action="/" method="POST">
          <label for="rotate">Rotate by:</label>
          <input id="rotate" type="text" name="rot"/>
          
          <textarea name="text">{0}</textarea>
          <input type="submit"/>
        
        
      
      </form>
    
      <!-- create your form here -->
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():    
    rotd = int(request.form['rot'])
    texted = str(request.form['text'])
    rotated = str(rotate_string(texted, rotd))
    return form.format(rotated)


app.run()    