from flask import Blueprint, render_template
from app.main_module.DateUtil import getTodaysDateAsString


main_bp = Blueprint('main_page', __name__)



@main_bp.route("/main", methods=["GET", "POST"])
@main_bp.route("/", methods=["GET", "POST"])
def main():
    print('in module_ex_1_bp')
    location = "images"
    date = getTodaysDateAsString()
    image_name = "{image_location}/{date}.jpeg".format(image_location=location, date=date)
    altered_image_name = "{image_location}/{date}altered.jpeg".format(image_location=location, date=date)

    return render_template("main_module/module.html", image_name=image_name, altered_image_name=altered_image_name)


