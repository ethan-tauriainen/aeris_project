import os
from pathlib import Path

IMG_PATH = Path("./flaskr")
IMG = IMG_PATH / "data.png"


def test_sum(client):
    response = client.get("/data/get-sum")
    assert response.json["sum"] == "0.000137476137616907"


def test_mean(client):
    response = client.get("/data/get-mean")
    assert response.json["mean"] == "1.414363555729496e-07"


def test_std_deviation(client):
    response = client.get("/data/get-std-deviation")
    assert response.json["std-deviation"] == "4.5936824115977264e-07"


def test_img(client):
    if (os.path.exists(IMG)):
        os.remove(IMG)
    
    assert not os.path.exists(IMG)
    response = client.get("/data/get-image")
    assert os.path.exists(IMG)
    assert response is not None
    assert response.mimetype == "image/png"

    os.remove(IMG)
