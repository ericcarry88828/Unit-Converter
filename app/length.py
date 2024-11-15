from flask import Blueprint, request, flash, render_template
from .units_cal import check_valid_input, units_of_length

bp = Blueprint('length', __name__)


@bp.route("/")
@bp.route("/convert-length", methods=['GET', 'POST'])
def convert_length():
    if request.method == "POST":
        number = request.form.get("number")
        convert_from = request.form.get("convert-from").lower()
        convert_to = request.form.get("convert-to").lower()
        valid, message = check_valid_input(
            "length", [number, convert_from, convert_to])
        if not valid:
            flash(message)
            return render_template("length.html")

        res = units_of_length(number, convert_from, convert_to)
        return render_template("length.html", result=res)
    return render_template("length.html", result=None)
