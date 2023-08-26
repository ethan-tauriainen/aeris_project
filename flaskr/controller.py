from flask import Blueprint

bp = Blueprint("controller", __name__, url_prefix="/data")


@bp.route("/get-sum", methods=["GET"])
def get_sum():
    return {"sum": "sum"}


@bp.route("/get-mean", methods=["GET"])
def get_mean():
    return {"mean": "mean"}


@bp.route("/get-std-deviation", methods=["GET"])
def get_std_deviation():
    return {"std-deviation": "std-deviation"}


@bp.route("/get-image", methods=["GET"])
def get_image():
    return {"image": "image.png"}
