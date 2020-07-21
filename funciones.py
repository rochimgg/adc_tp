import matplotlib.pyplot as plt

from constants import TIME_LABEL, AMPLITUDE_LABEL


def plot_2_signals(x, y1, y2, title, xlim=None, ylim=None, label=""):
    try:
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.plot(x, y1, color="orange", linewidth=2.5, linestyle="-", label=label)
        plt.plot(x, y2, color="royalblue", linewidth=2.5, linestyle="-", label="Respuesta")
        plt.legend(loc='upper right')
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
