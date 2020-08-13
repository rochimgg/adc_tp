import os

import matplotlib as mpl
import matplotlib.pyplot as plt

from constants import *
from functions import plot_2_signals, plot_2_signals_same_log_x, signal_csv2tex, bode_csv2tex, plot_multiple_signals

mpl.use("pgf")
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
    print(w_a[mag_a < -3 - 1.02][-1] / 2 / np.pi)


def q():
    d = dict(zip(w_a, mag_a))
    asy = 20 * np.log(gain_a)
    w1 = 1721.15
    w2 = 948.91
    q1 = d[w1] if w1 in d else d[min(d.keys(), key=lambda k: abs(k - w1))] - asy
    q2 = d[w2] if w2 in d else d[min(d.keys(), key=lambda k: abs(k - w2))] - asy
    print(QUALITY_FACTOR_MESSAGE)
    print("q1: " + str(q1))
    print("q2: " + str(q2))


#################
# Bode Diagrams #
#################


def bode_plot_analytic():
    plot_2_signals_same_log_x(w_a, mag_a, phase_a, BODE_PLOT_ANALYTIC_DIAGRAM_TITLE, xlim=(0.9e1, 1.8e4),
                              axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
                              file_name=BODE_PLOT_ANALYTIC_FILE_NAME)
    plot_2_signals_same_log_x(w_a, mag_a, phase_a, BODE_PLOT_ANALYTIC_DIAGRAM_ZOOM_TITLE, xlim=(1.8e2, 18e4),
                              y1lim=(-1.3, 0.2), y2lim=(-360, 0),
                              axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
                              file_name=BODE_PLOT_ZOOM_ANALYTIC_FILE_NAME)


def bode_plot_normalized():
    plot_2_signals_same_log_x(w_n, mag_n, phase_n, BODE_PLOT_NORMALIZED_DIAGRAM_TITLE, xlim=(0.9e1, 1.8e4),
                              axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
                              file_name=BODE_PLOT_NORMALIZED_FILE_NAME)
    plot_2_signals_same_log_x(w_n, mag_n, phase_n, BODE_PLOT_NORMALIZED_DIAGRAM_ZOOM_TITLE, xlim=(1.8e2, 18e4),
                              y1lim=(-1.3, 2.5), y2lim=(-360, 0),
                              axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
                              file_name=BODE_PLOT_ZOOM_NORMALIZED_FILE_NAME)


def bode_plot_real():
    bode_csv2tex("../ltspice/bode/filter_4th_order_mf_bode.csv", BODE_PLOT_REAL_DIAGRAM_TITLE,
                 axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
                 file_name=BODE_PLOT_REAL_FILE_NAME)
    bode_csv2tex("../ltspice/bode/filter_4th_order_mf_bode.csv", BODE_PLOT_REAL_DIAGRAM_ZOOM_TITLE, xlim=(1e2, 1e3),
                 y1lim=(-1.3, 2.5), axis_labels=(OMEGA_LABEL, MAGNITUDE_LABEL, PHASE_LABEL),
                 file_name=BODE_PLOT_ZOOM_REAL_FILE_NAME)


def bode_mag_analytic():
    plt.figure()
    plt.semilogx(w_a, mag_a, color="royalblue", linewidth=2.5, linestyle="-")
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(MAGNITUDE_LABEL)
    plt.title(MAGNITUDE_ANALYTIC_DIAGRAM_TITLE)
    plt.grid(True)
    plt.savefig("../latex/" + BODE_MAGNITUDE_ANALYTIC_FILE_NAME + '.pgf')
    plt.close()


def bode_phase_analytic():
    plt.figure()
    plt.semilogx(w_a, phase_a, color="royalblue", linewidth=2.5, linestyle="-")
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(PHASE_LABEL)
    plt.title(PHASE_ANALYTIC_DIAGRAM_TITLE)
    plt.grid(True)
    plt.savefig("../latex/" + BODE_PHASE_ANALYTIC_FILE_NAME + '.pgf')
    plt.close()


#################
#   Responses   #
#################

def step_response_analytic():
    fun = np.ones((len(t),))
    t_var, resp = sys_a.step(T=t)
    plot_2_signals(t_var, fun, resp, STEP_RESPONSE_ANALYTIC_DIAGRAM_TITLE, (-0.003, 0.06),
                   signal_labels=(STEP_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=STEP_ANALYTIC_FILE_NAME)


def step_response_normalized():
    fun = np.ones((len(t),))
    t_var, resp = sys_n.step(T=t)
    plot_2_signals(t_var, fun, resp, STEP_RESPONSE_NORMALIZED_DIAGRAM_TITLE, (-0.003, 0.06),
                   signal_labels=(STEP_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=STEP_NORMALIZED_FILE_NAME)


def step_response_real():
    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_step.csv")
    fun = np.ones((len(_t),))
    plot_2_signals(_t, fun, resp, STEP_RESPONSE_REAL_DIAGRAM_TITLE, (-0.003, 0.06),
                   signal_labels=(STEP_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=STEP_REAL_FILE_NAME)


def step_comparison():
    (t_a, resp_a) = sys_a.step(T=t)
    (t_n, resp_n) = sys_n.step(T=t)
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_step.csv")
    (t_c, resp_c) = t, -0.3322 * np.exp(-131.8 * t) * (np.cos(983.7 * t) + 0.4 * np.sin(983.7 * t)) + 1.22 * np.exp(
        -1018 * t) * (np.cos(1390 * t) - 0.41 * np.sin(1390 * t))
    coordinates = ((t_a, resp_a), (t_n, resp_n), (t_r, resp_r), (t_c, resp_c))
    plot_multiple_signals(coordinates, STEP_RESPONSE_COMPARISON_DIAGRAM_TITLE, (-0.003, 0.06), (-0.45, 1),
                          (TIME_LABEL, AMPLITUDE_LABEL), STEP_COMPARISON_NAME,
                          (ANALYTIC_LABEL, NORMALIZED_LABEL, REAL_LABEL, CALCULATED_LABEL))


def impulse_response_analytic():
    fun = signal.unit_impulse(shape=len(t), idx=0)
    t_var, resp = sys_a.impulse(T=t)
    plot_2_signals(t_var, fun, resp, IMPULSE_RESPONSE_ANALYTIC_DIAGRAM_TITLE, (-0.003, 0.06),
                   signal_labels=(IMPULSE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=IMPULSE_ANALYTIC_FILE_NAME)


def impulse_comparison():
    (t_a, resp_a) = sys_a.impulse(T=t)
    (t_c, resp_c) = t, -88.06 * np.exp(-131.8 * t) * (np.cos(983.7 * t) - 3.91 * np.sin(983.7 * t)) - 1961 * np.exp(
        -1018 * t) * (np.cos(1390 * t) + .6 * np.sin(1390 * t))
    plot_multiple_signals(((t_a, resp_a), (t_c, resp_c)), IMPULSE_RESPONSE_COMPARISON_DIAGRAM_TITLE, (-0.003, 0.06), None,
                          (TIME_LABEL, AMPLITUDE_LABEL), IMPULSE_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, CALCULATED_LABEL))


def sine_response_analytic():
    little_f0 = f0_a * 0.1
    great_f0 = f0_a * 100  # changed

    fun = np.sin(2 * np.pi * f0_a * t)
    resp = signal.lsim(sys_a, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_F0_ANALYTIC_DIAGRAM_TITLE, (-0.002, 0.04),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_F0_ANALYTIC_FILE_NAME)

    fun = np.sin(2 * np.pi * great_f0 * t)
    resp = signal.lsim(sys_a, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_GREAT_F0_ANALYTIC_DIAGRAM_TITLE, (-0.00002, 0.0004),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_GREAT_F0_ANALYTIC_FILE_NAME)

    fun = np.sin(2 * np.pi * little_f0 * t)
    resp = signal.lsim(sys_a, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_LITTLE_F0_ANALYTIC_DIAGRAM_TITLE, (-0.02, 0.4),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_LITTLE_F0_ANALYTIC_FILE_NAME)


def sine_response_real():
    little_f0 = f0_a * 0.1
    great_f0 = f0_a * 100  # changed
    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_sine_f0.csv")
    fun = np.sin(2 * np.pi * f0_a * _t)
    plot_2_signals(_t, fun, resp, SINE_RESPONSE_F0_REAL_DIAGRAM_TITLE, (-0.002, 0.04),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_F0_REAL_FILE_NAME)

    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_sine_100_times_f0.csv")
    fun = np.sin(2 * np.pi * great_f0 * _t)
    plot_2_signals(_t, fun, resp, SINE_RESPONSE_GREAT_F0_REAL_DIAGRAM_TITLE, (-0.00002, 0.0004),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_GREAT_F0_REAL_FILE_NAME)

    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_sine_f0_over_10.csv")
    fun = np.sin(2 * np.pi * little_f0 * _t)
    plot_2_signals(_t, fun, resp, SINE_RESPONSE_LITTLE_F0_REAL_DIAGRAM_TITLE, (-0.002, 0.04),
                   signal_labels=(SINE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SINE_LITTLE_F0_REAL_FILE_NAME)


def sine_response_comparison():
    little_f0 = f0_a * 0.1
    great_f0 = f0_a * 100  # changed

    fun = np.sin(2 * np.pi * f0_a * t)
    resp_a = signal.lsim(sys_a, fun, t)[1]
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_sine_f0.csv")
    plot_multiple_signals(((t_r, resp_r), (t, resp_a)), SINE_RESPONSE_F0_COMPARISON_DIAGRAM_TITLE, (-0.002, 0.04),
                          None, (TIME_LABEL, AMPLITUDE_LABEL), SINE_F0_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, REAL_LABEL))

    fun = np.sin(2 * np.pi * great_f0 * t)
    resp_a = signal.lsim(sys_a, fun, t)[1]
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_sine_100_times_f0.csv")
    (t_c, resp_c) = t, 0.89122 * np.sin(100 * 2 * np.pi * 138.62 * t + 0.026414)
    plot_multiple_signals(((t_r, resp_r), (t, resp_a), (t_c, resp_c)), SINE_RESPONSE_GREAT_F0_COMPARISON_DIAGRAM_TITLE,
                          (-0.00002, 0.0004),
                          None, (TIME_LABEL, AMPLITUDE_LABEL), SINE_GREAT_F0_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, REAL_LABEL, CALCULATED_LABEL))

    fun = np.sin(2 * np.pi * little_f0 * t)
    resp_a = signal.lsim(sys_a, fun, t)[1]
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_sine_f0_over_10.csv")
    plot_multiple_signals(((t_r, resp_r), (t, resp_a)), SINE_RESPONSE_LITTLE_F0_COMPARISON_DIAGRAM_TITLE, (-0.002, 0.04),
                          None, (TIME_LABEL, AMPLITUDE_LABEL), SINE_LITTLE_F0_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, REAL_LABEL))


def square_response_analytic():
    fun = signal.square(2 * np.pi * f0_a * t)
    resp = signal.lsim(sys_a, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_F0_ANALYTIC_DIAGRAM_TITLE, (-0.0017, 0.035),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_F0_ANALYTIC_FILE_NAME)

    fun = signal.square(2 * np.pi * f0_a * 10 * t)
    resp = signal.lsim(sys_a, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_10_TIMES_F0_ANALYTIC_DIAGRAM_TITLE, (-0.00017, 0.0035),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_10_TIMES_F0_ANALYTIC_FILE_NAME)

    fun = signal.square(2 * np.pi * f0_a / 10 * t)
    resp = signal.lsim(sys_a, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_F0_OVER_10_ANALYTIC_DIAGRAM_TITLE, (-0.017, 0.35),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_F0_OVER_10_ANALYTIC_FILE_NAME)


def square_response_real():
    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_square_f0.csv")
    fun = signal.square(2 * np.pi * f0_a * _t)

    plot_2_signals(_t, fun, resp, SQUARE_RESPONSE_F0_REAL_DIAGRAM_TITLE, (-0.0017, 0.035),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_F0_REAL_FILE_NAME)

    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_square_10_times_f0.csv")
    fun = signal.square(2 * np.pi * f0_a * 10 * _t)

    plot_2_signals(_t, fun, resp, SQUARE_RESPONSE_10_TIMES_F0_REAL_DIAGRAM_TITLE, (-0.00017, 0.0035),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_10_TIMES_F0_REAL_FILE_NAME)

    _t, resp = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_square_f0_over_10.csv")
    fun = signal.square(2 * np.pi * f0_a / 10 * _t)

    plot_2_signals(_t, fun, resp, SQUARE_RESPONSE_F0_OVER_10_REAL_DIAGRAM_TITLE, (-0.017, 0.35),
                   signal_labels=(SQUARE_LABEL, RESPONSE_LABEL), axis_labels=(TIME_LABEL, AMPLITUDE_LABEL),
                   file_name=SQUARE_F0_OVER_10_REAL_FILE_NAME)


def square_response_comparison():
    fun = signal.square(2 * np.pi * f0_a * t)
    resp_a = signal.lsim(sys_a, fun, t)[1]
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_square_f0.csv")
    plot_multiple_signals(((t_r, resp_r), (t, resp_a)), SQUARE_RESPONSE_F0_COMPARISON_DIAGRAM_TITLE, (-0.0017, 0.035),
                          None, (TIME_LABEL, AMPLITUDE_LABEL), SQUARE_F0_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, REAL_LABEL))

    fun = signal.square(2 * np.pi * f0_a * 10 * t)
    resp_a = signal.lsim(sys_a, fun, t)[1]
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_square_10_times_f0.csv")
    plot_multiple_signals(((t_r, resp_r), (t, resp_a)), SQUARE_RESPONSE_10_F0_COMPARISON_DIAGRAM_TITLE,
                          (-0.00017, 0.0035),
                          None, (TIME_LABEL, AMPLITUDE_LABEL), SQUARE_10_F0_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, REAL_LABEL))

    fun = signal.square(2 * np.pi * f0_a / 10 * t)
    resp_a = signal.lsim(sys_a, fun, t)[1]
    (t_r, resp_r) = signal_csv2tex("../ltspice/simulations/filter_4th_order_mf_square_f0_over_10.csv")
    plot_multiple_signals(((t_r, resp_r), (t, resp_a)), SQUARE_RESPONSE_F0_OVER_10_COMPARISON_DIAGRAM_TITLE,
                          (-0.017, 0.35),
                          None, (TIME_LABEL, AMPLITUDE_LABEL), SQUARE_F0_OVER_10_COMPARISON_FILE_NAME,
                          (ANALYTIC_LABEL, REAL_LABEL))


def main():
    impulse_comparison()
    step_comparison()
    square_response_comparison()
    sine_response_comparison()
    print("termine")


if __name__ == "__main__":  # execute only if run as a script
    main()
