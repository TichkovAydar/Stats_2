import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


def percent_formatter(X, pos):
    return '%2.0f %%' % (X * 100)


def bar(X, y):
    formatter = FuncFormatter(percent_formatter)
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(X, y)
    plt.xticks(X)
    plt.show()
