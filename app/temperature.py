from flask import Blueprint, request, flash, render_template
from .units_cal import check_valid_input, units_of_temperature

bp = Blueprint('temperature', __name__,)


@bp.route("/convert-temperature", methods=['GET', 'POST'])
def convert_temperature():
    if request.method == "POST":
        number = request.form.get("number")
        convert_from = request.form.get("convert-from").lower()
        convert_to = request.form.get("convert-to").lower()
        valid, message = check_valid_input(
            "temperature", [number, convert_from, convert_to])
        if not valid:
            flash(message)
            return render_template("temperature.html")

        res = units_of_temperature(number, convert_from, convert_to)
        return render_template("temperature.html", result=res)
    return render_template("temperature.html", result=None)
