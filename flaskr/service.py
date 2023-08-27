from pathlib import Path
import pandas
import matplotlib.pyplot as pyplot

CONCENTRATION_STR = "concentration"
PATH = Path("./flaskr/data")
CSV = PATH / "concentration.timeseries.csv"
IMG_PATH = Path("./flaskr")
IMG = IMG_PATH / "data.png"
POINTS = pandas.read_csv(CSV.as_posix())


def calculate_sum():
    return POINTS[CONCENTRATION_STR].sum()


def calculate_mean():
    return POINTS[CONCENTRATION_STR].mean()


def calculate_std_deviation():
    return POINTS[CONCENTRATION_STR].std()


def generate_png():
    
    x = POINTS["x"].values
    y = POINTS["y"].values
    concentration = POINTS[CONCENTRATION_STR].values

    fig, ax = pyplot.subplots()

    scatter = ax.scatter(x, y, c=concentration)

    legend = ax.legend(
        *scatter.legend_elements(), loc="upper right", title="Concentrations"
    )

    ax.add_artist(legend)
    ax.set_title("Aeris LLC Project Data Visualization")

    scatter.legend_elements(prop="sizes", alpha=0.6)

    pyplot.savefig(IMG, format="png")

    # TODO: Calculate MD5 Sum of the resulting .png
