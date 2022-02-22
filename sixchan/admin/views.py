from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.get("/report")
def report():
    return "report"
