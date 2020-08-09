import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from constants import COLOR_SIGNAL_1, COLOR_SIGNAL_2

mpl.use("pgf")
os.environ["PATH"] += os.pathsep + '/usr/local/texlive/2020/bin/x86_64-darwin'


def plot_2_signals(x, y1, y2, title, xlim=None, ylim=None, signal_labels=("", ""), axis_labels=("", ""), file_name=""):
    try:
        plt.plot(x, y1, color=COLOR_SIGNAL_1, linewidth=2.5, linestyle="-", label=signal_labels[0])
        plt.plot(x, y2, color=COLOR_SIGNAL_2, linewidth=2.5, linestyle="-", label=signal_labels[1])
        plt.legend(loc='upper right')
        plt.xlabel(axis_labels[0])
        plt.ylabel(axis_labels[1])
        plt.title(title)
        if xlim is not None:
            plt.xlim(*xlim)
        if ylim is not None:
            plt.ylim(*ylim)
        plt.grid(True)
        plt.savefig("../latex/images/graphics/" + file_name + '.pgf')
        plt.close()
    except EOFError:
        print("plot_2_signals_failed")


def plot_2_signals_same_log_x(x, y1, y2, title, xlim=None, axis_labels=("", "", ""), file_name=""):
    try:
        fig, ax1 = plt.subplots()
        plt.title(title)
        if xlim is not None:
            plt.xlim(*xlim)
        ax1.set_xlabel(axis_labels[0])
        ax1.set_ylabel(axis_labels[1], color=COLOR_SIGNAL_1)
        ax1.semilogx(x, y1, color=COLOR_SIGNAL_1, linewidth=2.5, linestyle="-")
        ax1.tick_params(axis='y', labelcolor=COLOR_SIGNAL_1)

        ax2 = ax1.twinx()

        ax2.set_ylabel(axis_labels[2], color=COLOR_SIGNAL_2)
        ax2.semilogx(x, y2, color=COLOR_SIGNAL_2, linewidth=2.5, linestyle="-")
        ax2.tick_params(axis='y', labelcolor=COLOR_SIGNAL_2)

        fig.tight_layout()
        plt.show()
        plt.grid(True)
        plt.savefig("../latex/images/graphics/" + file_name + '.pgf')
        plt.close()
    except EOFError:
        print("plot_2_signals_same_log_x() failed")
