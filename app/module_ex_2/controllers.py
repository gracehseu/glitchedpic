from flask import Blueprint, render_template
from datetime import date

module_ex_2_bp = Blueprint('module_ex_2', __name__)

@module_ex_2_bp.route("/module_ex_2_bp", methods=["GET", "POST"])
def main():
    # passes the date to the jinja2 template
    print('in module_ex_2_bp')
    what_is_day = date.today().strftime("%B %d, %Y")

    return render_template("module_ex_2/module.html", date=what_is_day)