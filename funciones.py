import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from constants import TIME_LABEL, AMPLITUDE_LABEL


def plot_response(function, system, f=0, title="", xlim_sup=10):

    t = np.linspace(0, 1, 1000000, endpoint=False)
    duty = np.ones((1000000,))
    xlim_inf = 0.5
    t_var = t
    fun = 0
    resp = 0

    try:
        if function == "sine":
            fun = np.sin(2 * np.pi * f * t)
            resp = signal.lsim(system, fun, t)[1]
        if function == "square":
            fun = signal.square(2 * np.pi * f * t)
            resp = signal.lsim(system, fun, t)[1]
        if function == "step":
            # TODO: CHANGEME
            fun = signal.square(2 * np.pi * f * t, duty)
            resp, t_var = system.step()
        if function == "impulse":
            fun = signal.unit_impulse(100, 'mid')
            resp, t_var = system.impulse()
        plt.plot(t_var, fun)
        plt.plot(t_var, resp)
        plt.xlabel(TIME_LABEL)
        plt.ylabel(AMPLITUDE_LABEL)
        plt.title(title)
       # plt.ylim(-2, 2)
       # plt.xlim(xlim_inf, xlim_sup)
        plt.grid()
        plt.show()
    except EOFError:
        print("plot_response failed")


def plot_2_signals(x, y1, y2, title, xlim=None, ylim=None, function = ""):
    try:
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.plot(x, y1, color="orange", linewidth=2.5, linestyle="-", label=function)
        plt.plot(x, y2, color="blue",  linewidth=2.5, linestyle="-", label="Respuesta")
        plt.legend(loc='upper left')
        plt.xlabel(TIME_LABEL)
        plt.ylabel(AMPLITUDE_LABEL)
        plt.title(title)
        if xlim is not None:
            plt.xlim(*xlim)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.grid()
        plt.show()
    except EOFError:
        print("plot_2_signals_failed")




