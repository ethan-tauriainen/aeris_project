from flaskr import service
from pathlib import Path
import os

IMG_PATH = Path("./flaskr")
IMG = IMG_PATH / "data.png"


def test_img_creation():
    if os.path.exists(IMG):
        os.remove(IMG)

    assert not os.path.exists(IMG)
    service.generate_png()
    assert os.path.exists(IMG)
    os.remove(IMG)
