"""Route for handling orders"""
from flask import Blueprint
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="/")


@bp.route("/")
@login_required
def index():
    """Index route"""
    return "Order Up!"
