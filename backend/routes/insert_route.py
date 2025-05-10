# routes/insert_route.py
from flask import Blueprint
from controllers.insert_controller import insert_data

insert_bp = Blueprint("insert", __name__)

insert_bp.route("/api/insert", methods=["POST"])(insert_data)
