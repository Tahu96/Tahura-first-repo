from flask import Flask
app = Flask(__name__)
@app.route('/')
def run():
 return "<h1>Hello Python main.py</h1>"
app.run(port="3000",debug=True)