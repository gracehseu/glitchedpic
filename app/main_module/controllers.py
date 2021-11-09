from flask import Blueprint, render_template
from app.main_module.image_config import IMAGE_LOCATION

main_bp = Blueprint('main_page', __name__)


@main_bp.route("/main", methods=["GET", "POST"])
@main_bp.route("/", methods=["GET", "POST"])
def main():
    print('in module_ex_1_bp')
    image_name = "Love of Winter.jpeg"
    location = "images"

    return render_template("main_module/module.html", image_name="{}/{}".format(location, image_name), altered_image_name="{}/{}{}".format(location, "altered", image_name))
