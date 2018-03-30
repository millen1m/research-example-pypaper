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

    length = 10.
    width = 5.0  # metres
    depth_shallow = 1.0  # metres
    depth_deep = 2.0  # metres

    cohesion = 0
    unit_weight = 18.5  # submerged

    fd_shallow = geofound.create_foundation(length, width, depth_shallow)
    fd_deep = geofound.create_foundation(length, width, depth_deep)

    friction_angles = np.linspace(start=32, stop=38, num=30)  # create an array of friction angles between 32-38

    q_lims_shallow = []  # Create an empty list to store values of the ultimate bearing pressure
    q_lims_deep = []

    for i in range(len(friction_angles)):
        phi = friction_angles[i]
        sl = geofound.create_soil(phi, cohesion, unit_weight)
        sl.unit_sat_weight = 18.5  # kN/m3

        # Solve the bearing capacity using the Vesic's method
        # Long foundation
        q_lim_shallow = geofound.capacity.vesics_1975(sl, fd_shallow)
        q_lims_shallow.append(q_lim_shallow)

        # Short foundation
        q_lim_deep = geofound.capacity.vesics_1975(sl, fd_deep)
        q_lims_deep.append(q_lim_deep)

    bf, subplot = plt.subplots()  # Create a subplot
    subplot.plot(friction_angles, q_lims_shallow, label="Shallow foundation", c=cbox(0))
    subplot.plot(friction_angles, q_lims_deep, label="Deep foundation", c=cbox(1), ls="--")

    subplot.set_xlabel('Friction angle [degrees]')
    # subplot.set_xscale('log')  # Can plot in log-scale
    subplot.set_ylabel('Ultimate bearing capacity [kPa]')
    ef.xy(subplot, x_origin=False, y_origin=True)
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
    create(save=2, show=1)

