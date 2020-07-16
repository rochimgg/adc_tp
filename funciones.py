import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from constants import TIME_LABEL, AMPLITUDE_LABEL


def plot_response(function, system, f, x, title, xlim_sup):
    xlim_inf = 0.5
    x_var = x
    fun = 0
    resp = 0
    try:
        if function == "sine":
            fun = np.sin(2 * np.pi * f * x)
            resp = signal.lsim(system, fun, x)[1]
        if function == "square":
            fun = signal.square(2 * np.pi * f * x)
            resp = signal.lsim(system, fun, x)[1]
        if function == "step":
            # TODO: CHANGEME
            resp, x_var = system.step()
        if function == "impulse":
            fun = signal.unit_impulse(100, 'mid')
            resp, x_var = system.impulse()
        plt.plot(x_var, fun)
        plt.plot(x_var, resp)
        plt.xlabel(TIME_LABEL)
        plt.ylabel(AMPLITUDE_LABEL)
        plt.title(title)
        plt.ylim(-2, 2)
        plt.xlim(xlim_inf, xlim_sup)
        plt.grid()
        plt.show()
    except EOFError:
        print("plot_response failed")
