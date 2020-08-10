import csv
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
from constants import *

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


def plot_2_signals_same_log_x(x, y1, y2, title, xlim=None, y1lim=None, y2lim=None, axis_labels=("", "", ""), file_name=""):
    try:
        fig, ax1 = plt.subplots()
        plt.title(title)
        if xlim is not None:
            plt.xlim(*xlim)
        if y1lim is not None:
            plt.ylim(*y1lim)
        ax1.set_xlabel(axis_labels[0])
        ax1.set_ylabel(axis_labels[1], color=COLOR_SIGNAL_1)
        ax1.semilogx(x, y1, color=COLOR_SIGNAL_1, linewidth=2.5, linestyle="-")
        ax1.tick_params(axis='y', labelcolor=COLOR_SIGNAL_1)

        ax2 = ax1.twinx()
        if y2lim is not None:
            plt.ylim(*y2lim)
        ax2.set_ylabel(axis_labels[2], color=COLOR_SIGNAL_2)
        ax2.semilogx(x, y2, color=COLOR_SIGNAL_2, linewidth=2.5, linestyle="-")
        ax2.tick_params(axis='y', labelcolor=COLOR_SIGNAL_2)

        fig.tight_layout()
        plt.grid(True)
        plt.savefig("../latex/images/graphics/" + file_name + '.pgf')
        plt.close()
    except EOFError:
        print("plot_2_signals_same_log_x() failed")


def csv2tex(file_path, title, xlim=None, y1lim=None, y2lim=None, axis_labels=("", "", ""), file_name=""):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        _w = []
        _mag = []
        _phase = []

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {" ,".join(row)}')
                line_count += 1
            else:
                _w.append(float(row[0]))
                _mag.append(float(row[1].split(",")[0].replace("dB", "").replace("(", "")))
                _phase_number = float(row[1].split(",")[1].replace("∞)", ""))
                if _phase_number > 0:
                    _phase_number = _phase_number - 360
                _phase.append(_phase_number)
                print(f'\t{row[0]} \t {row[1]} \n')
                line_count += 1
        print(f'Processed {line_count} lines.')
        plot_2_signals_same_log_x(_w, _mag, _phase, title, xlim, y1lim, y2lim, axis_labels, file_name)


def main():
    csv2tex("../ltspice/filter_4th_order_mf_bode.csv", "BODE SPICE", axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
            file_name="BODE_SPICE")


if __name__ == "__main__":  # execute only if run as a script
    main()
