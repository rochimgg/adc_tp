import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from constants import *

p = [0.8911, 0, 0, 0, 0]
q = [1, 2539, 4.686e6, 2.894e9, 2.863e12]
sys = signal.TransferFunction(p, q)
w, mag, phase = signal.bode(sys)
w0 = w[mag < -3][-1]

#################
# Bode Diagrams #
#################

# Gain diagram
plt.figure()
plt.semilogx(w, mag)
plt.xlabel(ANGULAR_FREQUENCY_LABEL)
plt.ylabel(GAIN_LABEL)
plt.title(GAIN_DIAGRAM_TITLE)
plt.grid()
plt.show()

# Phase diagram
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

# Step response

t, y = sys.step()
plt.plot(t, y)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(STEP_RESPONSE_DIAGRAM_TITLE)
plt.grid()
plt.show()

# Respuesta al impulso

t, y = sys.impulse()
plt.plot(t, y)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(IMPULSE_RESPONSE_DIAGRAM_TITLE)
plt.grid()
plt.show()

t = np.linspace(0, 1, 1000000, endpoint=False)

sq_resp_f0 = signal.lsim(sys, signal.square(w0 * t), t)[1]
sq_resp_10_times_f0 = signal.lsim(sys, signal.square(10 * w0 * t), t)[1]
sq_resp_f0_over_10 = signal.lsim(sys, signal.square(w0 / 10 * t), t)[1]

# Response to squared signal with frequency f0
plt.plot(t, sq_resp_f0)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(SQUARE_RESPONSE_F0_DIAGRAM_TITLE)
plt.ylim(-2, 2)
plt.xlim(0, 0.04)
plt.grid()
plt.show()

# Response to squared signal with frequency 10*f0
plt.plot(t, sq_resp_10_times_f0)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE)
plt.ylim(-2, 2)
plt.xlim(0, 0.01)
plt.grid()
plt.show()

# Response to squared signal with frequency f0/10
plt.plot(t, sq_resp_f0_over_10)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE)
plt.ylim(-2, 2)
plt.xlim(0, 0.2)
plt.grid()
plt.show()

f = w0 / (2 * np.pi)
little_f = f * 0.1
great_f = f * 1000

sin_little_f0 = np.sin(w0 * 0.1 * t)
sin_f0 = np.sin(w0 * t)
sin_great_f0 = np.sin(w0 * 10000 * t)

sin_resp_little_f0 = signal.lsim(sys, sin_little_f0, t)[1]
sin_resp_f0 = signal.lsim(sys, sin_f0, t)[1]
sin_resp_great_f0 = signal.lsim(sys, sin_great_f0, t)[1]

# Response to sinusoidal signal with frequency 0.1*f0
plt.plot(t, sin_little_f0)
plt.plot(t, sin_resp_little_f0)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(SINE_RESPONSE_LITTLE_F0_TITLE)
plt.ylim(-2, 2)
plt.xlim(0.5, 0.501)
plt.grid()
plt.show()

# Response to sinusoidal signal with frequency f0
plt.plot(t, sin_f0)
plt.plot(t, sin_resp_f0)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(SINE_RESPONSE_F0_DIAGRAM_TITLE)
plt.ylim(-2, 2)
plt.xlim(0.5, 0.04)
plt.grid()
plt.show()

# Response to sinusoidal signal with frequency 10000*f0
plot_sinusoidal_response(sys, great_f, t, SINE_RESPONSE_GREAT_F0_TITLE, 0.01)
plt.plot(t, sin_great_f0)
plt.plot(t, sin_resp_great_f0)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(SINE_RESPONSE_GREAT_F0_TITLE)
plt.ylim(-2, 2)
plt.xlim(0.5, 0.01)
plt.grid()
plt.show()


def plot_sinusoidal_response(system, f, x, title, xlim_sup):
    sin = np.sin(2 * np.pi * f * x)
    sin_resp = signal.lsim(system, sin, x)[1]
    plt.plot(t, sin)
    plt.plot(t, sin_resp)
    plt.xlabel(TIME_LABEL)
    plt.ylabel(AMPLITUDE_LABEL)
    plt.title(title)
    plt.ylim(-2, 2)
    plt.xlim(0.5, xlim_sup)
    plt.grid()
    plt.show()
