from flask import Blueprint, Flask
from . import service

bp = Blueprint("controller", __name__, url_prefix="/data")
app = Flask(__name__)


@bp.route("/get-sum", methods=["GET"])
def get_sum():
    sum = service.calculate_sum()
    app.logger.debug(f"Calculated sum: {sum}")
    return {"sum": f"{sum}"}


@bp.route("/get-mean", methods=["GET"])
def get_mean():
    mean = service.calculate_mean()
    app.logger.debug(f"Calculated mean: {mean}")
    return {"mean": f"{mean}"}


@bp.route("/get-std-deviation", methods=["GET"])
def get_std_deviation():
    std_deviation = service.calculate_std_deviation()
    app.logger.debug(f"Calculated std deviation: {std_deviation}")
    return {"std-deviation": f"{std_deviation}"}


@bp.route("/get-image", methods=["GET"])
def get_image():
    service.generate_png()
    return {"image": "image.png"}
