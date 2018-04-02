import numpy as np
import matplotlib.pyplot as plt
from bwplot import cbox
import all_paths as ap
import engformat as ef
import settings as ops

import geofound
import geofound.settlement
import geofound.capacity


def create(save=0, show=0):
    name = "large_random_database"
    data = np.loadtxt(ap.PROJECT_LARGE_DATABASE + name + ".txt", delimiter=",")
    a = data[:, 0]  # load the first column as 'a'
    b = data[:, 1]  # load the second column as 'a'
    print(a)
    bf, subplot = plt.subplots()  # Create a subplot
    subplot.plot(a, b, 'o', label="data", c=cbox(0))

    subplot.set_xlabel('a')
    # subplot.set_xscale('log')  # Can plot in log-scale
    subplot.set_ylabel('b')
    ef.xy(subplot, x_origin=True, y_origin=True, parity=True)
    ef.revamp_legend(subplot, loc="upper left", prop={'size': 9})  # change adjust position and font size

    bf.tight_layout()
    name = __file__.replace('.py', '')
    name = name.split("figure_")[-1]
    extension = ""
    if save == 2:
        ef.save_figure(ap, bf, name, publish=True, name_ext=extension, ftype=ops.PUBLICATION_FILE_TYPE,
                       latex=False, dpi=ops.PUBLICATION_DPI)
    elif save == 1:
        ef.save_figure(ap, bf, name, name_ext="")
    if show:
        plt.show()


if __name__ == '__main__':
    create(save=0, show=1)

