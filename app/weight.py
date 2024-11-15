from flask import Blueprint, request, flash, render_template
from .units_cal import check_valid_input, units_of_weight

bp = Blueprint('weight', __name__)


@bp.route("/convert-weight", methods=['GET', 'POST'])
def convert_weight():
    if request.method == "POST":
        number = request.form.get("number")
        convert_from = request.form.get("convert-from").lower()
        convert_to = request.form.get("convert-to").lower()
        valid, message = check_valid_input(
            "weight", [number, convert_from, convert_to])
        if not valid:
            flash(message)
            return render_template("weight.html")

        res = units_of_weight(number, convert_from, convert_to)
        return render_template("weight.html", result=res)
    return render_template("weight.html", result=None)
