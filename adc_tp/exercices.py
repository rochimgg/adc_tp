import os

import matplotlib.pyplot as plt

from constants import *
from functions import plot_2_signals, plot_2_signals_same_log_x

# mpl.use("pgf")
os.environ["PATH"] += os.pathsep + '/usr/local/texlive/2020/bin/x86_64-darwin'


def main():
    pass


#####################
# Filter Parameters #
#####################

def poles():
    p = [0.8911, 0, 0, 0, 0]
    q = [1, 2539, 4.686e6, 2.894e9, 2.863e12]
    zeros, poles, gain = signal.tf2zpk(p, q)
    print(POLES_MESSAGE)
    print(poles)


def zeros():
    p = [0.8911, 0, 0, 0, 0]
    q = [1, 2539, 4.686e6, 2.894e9, 2.863e12]
    zeros, poles, gain = signal.tf2zpk(p, q)
    print(ZEROS_MESSAGE)
    print(zeros)


def omega_0():
    print(OMEGA_ZERO_MESSAGE)
    print(w[mag < -3][-1])


def q():
    pass


#################
# Bode Diagrams #
#################

def bode_plot():
    plot_2_signals_same_log_x(w, mag, phase, BODE_PLOT_DIAGRAM_TITLE, xlim=(1e0, 1e6),
                              axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL), file_name=BODE_PLOT_FILE_NAME)


def bode_mag():
    plt.figure()
    plt.semilogx(w, mag, color="royalblue", linewidth=2.5, linestyle="-")
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(MAGNITUDE_LABEL)
    plt.title(MAGNITUDE_DIAGRAM_TITLE)
    plt.grid(True)
    plt.savefig("../latex/" + BODE_MAGNITUDE_FILE_NAME + '.pgf')
    plt.close()


def bode_phase():
    plt.figure()
    plt.semilogx(w, phase, color="royalblue", linewidth=2.5, linestyle="-")
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(PHASE_LABEL)
    plt.title(PHASE_DIAGRAM_TITLE)
    plt.grid(True)
    plt.savefig("../latex/" + BODE_PHASE_FILE_NAME + '.pgf')
    plt.close()


#################
#   Responses   #
#################

def step_response():
    fun = np.ones((len(t),))
    t_var, resp = sys.step(T=t)
    plot_2_signals(t_var, fun, resp, STEP_RESPONSE_DIAGRAM_TITLE, (-0.003, 0.06),
                   signal_labels=(STEP_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=STEP_FILE_NAME)


def impulse_response():
    fun = signal.unit_impulse(shape=len(t), idx=0)
    t_var, resp = sys.impulse(T=t)
    plot_2_signals(t_var, fun, resp, IMPULSE_RESPONSE_DIAGRAM_TITLE, (-0.003, 0.06),
                   labels=(IMPULSE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=IMPULSE_FILE_NAME)


def sine_response():
    little_f0 = f0 * 0.1
    great_f0 = f0 * 100  # changed

    fun = np.sin(2 * np.pi * f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_F0_DIAGRAM_TITLE, (-0.002, 0.04),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_F0_FILE_NAME)

    fun = np.sin(2 * np.pi * great_f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_GREAT_F0_TITLE, (-0.00002, 0.0004),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_GREAT_F0_FILE_NAME)

    fun = np.sin(2 * np.pi * little_f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_LITTLE_F0_TITLE, (-0.02, 0.4),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_LITTLE_F0_FILE_NAME)


def square_response():
    fun = signal.square(2 * np.pi * f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_F0_DIAGRAM_TITLE, (-0.0017, 0.035),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_F0_FILE_NAME)

    fun = signal.square(2 * np.pi * f0 * 10 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE, (-0.00017, 0.0035),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_10_TIMES_F0_FILE_NAME)

    fun = signal.square(2 * np.pi * f0 / 10 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE, (-0.017, 0.35),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_F0_OVER_10_FILE_NAME)


if __name__ == "__main__":  # execute only if run as a script
    main()
