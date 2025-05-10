from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import psycopg2

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL using environment variables
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api/test-db")
def test_db():
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    return jsonify({"postgres_version": version})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
