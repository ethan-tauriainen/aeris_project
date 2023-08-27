from flask import Blueprint, Flask, send_file, abort, jsonify, Response
from flaskr import service
from pathlib import Path
import os

IMG_PATH = Path("./flaskr")
IMG = IMG_PATH / "data.png"

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
    if os.path.exists(IMG):
        app.logger.debug(f"File: {IMG} created, sending to client")
        return send_file("data.png", mimetype="image/png")
    else:
        app.logger.error(f"Error creating file: {IMG}")
        abort(404, description="Image resource not located")
