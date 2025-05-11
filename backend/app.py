# app.py
#this is the python version of server.js for javascript
from flask import Flask
from flask_cors import CORS
from routes.insert_route import insert_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(insert_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
