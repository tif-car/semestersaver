# controllers/insert_controller.py
from flask import jsonify, request
from models.db import get_db_connection

def insert_data():
    data = request.get_json()  # Get the data sent by the frontend
    task = data["task"]  # Extract the task data from the request

    try:
        # Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the task into the tasks table
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()

        # Clean up by closing the cursor and connection
        cursor.close()
        conn.close()

        # Return a success message
        return jsonify({"message": "Task inserted successfully!"}), 201
    except Exception as e:
        # Return an error message if something goes wrong
        return jsonify({"message": f"Error inserting task: {str(e)}"}), 500

