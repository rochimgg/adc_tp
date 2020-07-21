import matplotlib.pyplot as plt

from constants import *
from funciones import plot_2_signals


def main(argv):

    zeros, poles, gain = signal.tf2zpk(p, q)
    print(POLES_MESSAGE + poles)


#################
# Bode Diagrams #
#################

def bode_mag():
    plt.figure()
    plt.semilogx(w, mag)
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(GAIN_LABEL)
    plt.title(GAIN_DIAGRAM_TITLE)
    plt.grid()
    plt.show()


def bode_phase():
    plt.figure()
    plt.semilogx(w, phase)
    plt.xlabel(ANGULAR_FREQUENCY_LABEL)
    plt.ylabel(PHASE_LABEL)
    plt.title(PHASE_DIAGRAM_TITLE)
    plt.grid()
    plt.show()

#################
#   Responses   #
#################

def step_response():
    fun = np.ones((len(t),))
    t_var, resp = sys.step(T=t)
    plot_2_signals(t_var, fun, resp, STEP_RESPONSE_DIAGRAM_TITLE, (-0.003, 0.06), label=STEP_LABEL)


def impulse_response():
    fun = signal.unit_impulse(shape=len(t), idx=0)
    t_var, resp = sys.impulse(T=t)
    plot_2_signals(t_var, fun, resp, IMPULSE_RESPONSE_DIAGRAM_TITLE, (-0.003, 0.06), label=IMPULSE_LABEL)


def sine_response():
    little_f0 = f0 * 0.1
    great_f0 = f0 * 100  # changed

    fun = np.sin(2 * np.pi * f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_F0_DIAGRAM_TITLE, (-0.002, 0.04), label=SINE_LABEL)

    fun = np.sin(2 * np.pi * great_f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_GREAT_F0_TITLE, (-0.00002, 0.0004), label=SINE_LABEL)

    fun = np.sin(2 * np.pi * little_f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SINE_RESPONSE_LITTLE_F0_TITLE, (-0.02, 0.4), label=SINE_LABEL)


def square_response():
    fun = signal.square(2 * np.pi * f0 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_F0_DIAGRAM_TITLE, (-0.0017, 0.035), label=SQUARE_LABEL)

    fun = signal.square(2 * np.pi * f0 * 10 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE, (-0.00017, 0.0035), label=SQUARE_LABEL)

    fun = signal.square(2 * np.pi * f0 / 10 * t)
    resp = signal.lsim(sys, fun, t)[1]
    plot_2_signals(t, fun, resp, SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE, (-0.017, 0.35), label=SQUARE_LABEL)


def poles():
    ret = signal.tf2zpk(q,p)
    print(POLES_MESSAGE + poles)


def zeros():
    dt, gain, poles, zeros = signal.tf2zpk(p, q)
    print(ZEROS_MESSAGE + zeros)


def omega_0():
    pass


def q():
    pass


if __name__ == "__main__":
    # execute only if run as a script
    main("")
