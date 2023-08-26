from pathlib import Path
import pandas
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pyplot
from matplotlib.colors import ListedColormap

CONCENTRATION_STR = "concentration"
PATH = Path("./flaskr/data")
CSV = PATH / "concentration.timeseries.csv"
POINTS = pandas.read_csv(CSV.as_posix())


def calculate_sum():
    return POINTS[CONCENTRATION_STR].sum()


def calculate_mean():
    return POINTS[CONCENTRATION_STR].mean()


def calculate_std_deviation():
    return POINTS[CONCENTRATION_STR].std()


def generate_png():
    """Use matplotlib to generate .png image of data

    Referenced matplotlib documentation:
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#sphx-glr-gallery-lines-bars-and-markers-scatter-with-legend-py
    """

    x = POINTS["x"].values
    y = POINTS["y"].values
    concentration = POINTS[CONCENTRATION_STR].values

    fig, ax = pyplot.subplots()

    scatter = ax.scatter(x, y, c=concentration)

    legend = ax.legend(
        *scatter.legend_elements(), loc="upper right", title="Concentrations"
    )

    ax.add_artist(legend)

    scatter.legend_elements(prop="sizes", alpha=0.6)

    pyplot.show()
