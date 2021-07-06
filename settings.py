import os

this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl

FIGURE_PATH = os.path.join(this_dir, 'figures')
STYLE_PATH = os.path.join(this_dir, 'conlab.mplstyle')
