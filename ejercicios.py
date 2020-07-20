import matplotlib.pyplot as plt
import numpy as np

from constants import *
from funciones import plot_2_signals


def main(argv):

    w, mag, phase = signal.bode(sys)
    w0 = w[mag < -3][-1]
    f0 = w0 / (2 * np.pi)

    #################
    #   Responses   #
    #################

    t = np.linspace(0, 1, 1000000, endpoint=False)
    fun = np.ones((len(t),))
    t_var, resp = sys.step(T=t)
    plot_2_signals(t_var, fun, resp, STEP_RESPONSE_DIAGRAM_TITLE, (-0.0005, 0.1))

    fun = signal.unit_impulse(shape=1000000, idx=0)
    fun2 = [1000000000] + np.zeros(len(t)-1)
    t_var, resp = sys.impulse(T=t)
    plot_2_signals(t_var, fun, resp, IMPULSE_RESPONSE_DIAGRAM_TITLE, (-0.0005, 0.1))

    little_f0 = f0 * 0.1
    great_f0 = f0 * 100  #changed

    fun = np.sin(2 * np.pi * f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t_var, fun, resp, SINE_RESPONSE_F0_DIAGRAM_TITLE, (-0.002, 0.04))

    fun = np.sin(2 * np.pi * great_f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t_var, fun, resp, SINE_RESPONSE_GREAT_F0_TITLE, (-0.00003, 0.0006))

    fun = np.sin(2 * np.pi * little_f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t_var, fun, resp, SINE_RESPONSE_LITTLE_F0_TITLE, (-0.03, 0.6))

    fun = signal.square(2 * np.pi * f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t_var, fun, resp, SQUARE_RESPONSE_F0_DIAGRAM_TITLE, (-0.0025, 0.05))

    fun = signal.square(2 * np.pi * f0 * 10 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t_var, fun, resp, SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE, (-0.0003, 0.006))

    fun = signal.square(2 * np.pi * f0 / 10 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t_var, fun, resp, SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE, (-0.015, 0.3))

    xlim_inf = 0.5
    t_var = t
    fun = 0
    resp = 0

    # Impulse response
    #   plot_response("impulse", sys, title=IMPULSE_RESPONSE_DIAGRAM_TITLE, xlim_sup=0.55)

    # Step response
    #   plot_response("step", sys, title=STEP_RESPONSE_DIAGRAM_TITLE, xlim_sup=0.55)

    # Response to squared signal with frequency f0
    #    plot_response("square", sys, f0, SQUARE_RESPONSE_F0_DIAGRAM_TITLE, 0.04)

    # Response to squared signal with frequency 10*f0
    #   plot_response("square", sys, 10*f0, SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE, 0.01)

    # Response to squared signal with frequency f0/10
    #    plot_response("square", sys, f0/10, SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE, 0.2)

    f0 = w0 / (2 * np.pi)
    little_f0 = f0 * 0.1
    great_f0 = f0 * 1000

    # Response to sinusoidal signal with frequency 0.1*f0


#   plot_response("sine", sys, little_f0, SINE_RESPONSE_LITTLE_F0_TITLE, 0.501)

# Response to sinusoidal signal with frequency f0
#   plot_response("sine", sys, f0, SINE_RESPONSE_F0_DIAGRAM_TITLE, 0.04)

# Response to sinusoidal signal with frequency 10000*f0
#  plot_response("sine", sys, great_f0, t, SINE_RESPONSE_GREAT_F0_TITLE, 0.01)

#################
# Bode Diagrams #
#################

def bode_mag():
    w, mag, phase = signal.bode(sys)
    plt.figure()
    plt.semilogx(w, mag)
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(GAIN_LABEL)
    plt.title(GAIN_DIAGRAM_TITLE)
    plt.grid()
    plt.show()


def bode_phase():
    w, mag, phase = signal.bode(sys)
    plt.figure()
    plt.semilogx(w, phase)
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(PHASE_LABEL)
    plt.title(PHASE_DIAGRAM_TITLE)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main("")
