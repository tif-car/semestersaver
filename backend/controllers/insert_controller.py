# controllers/insert_controller.py
from flask import jsonify, request
from models.db import get_db_connection

def insert_data():
    data = request.get_json()  # Get the data sent by the frontend
    name = data["name"]
    email = data["email"]

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO your_table_name (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Data inserted successfully!"})
    except Exception as e:
        return jsonify({"message": f"Error inserting data: {e}"}), 500
