from os.path import join
from time import time
import matplotlib.pyplot as plt

from settings import FIGURE_PATH, STYLE_PATH


def savefig(filename=None, fig=None, *args, **kwargs):
    if filename is None:
        filename = 'figure_' + str(round(time()*1000))
    if fig is None:
        fig = plt.gcf()
    path_out = join(FIGURE_PATH, filename)
    fig.savefig(path_out, *args, **kwargs)


def plt_reset():
    plt.close('all')
    plt.style.use(STYLE_PATH)
