import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from funciones import plot_response

from constants import *

p = [0.8911, 0, 0, 0, 0]
q = [1, 2539, 4.686e6, 2.894e9, 2.863e12]
sys = signal.TransferFunction(p, q)
w, mag, phase = signal.bode(sys)
w0 = w[mag < -3][-1]
f0 = w0 / (2 * np.pi)

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
plot_response("step", sys, title=STEP_RESPONSE_DIAGRAM_TITLE, xlim_sup=0.55)

t, y = sys.step()
plt.plot(t, y)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(STEP_RESPONSE_DIAGRAM_TITLE)
plt.grid()
plt.show()

# Impulse response
plot_response("impulse", sys, title=IMPULSE_RESPONSE_DIAGRAM_TITLE, xlim_sup=0.55)
t, y = sys.impulse()
plt.plot(t, y)
plt.xlabel(TIME_LABEL)
plt.ylabel(AMPLITUDE_LABEL)
plt.title(IMPULSE_RESPONSE_DIAGRAM_TITLE)
plt.grid()
plt.show()

t = np.linspace(0, 1, 1000000, endpoint=False)

# Response to squared signal with frequency f0
plot_response("square", sys, f0, t, SQUARE_RESPONSE_F0_DIAGRAM_TITLE, 0.04)

# Response to squared signal with frequency 10*f0
plot_response("square", sys, 10*f0, t, SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE, 0.01)

# Response to squared signal with frequency f0/10
plot_response("square", sys, f0/10, t, SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE, 0.2)

f0 = w0 / (2 * np.pi)
little_f0 = f0 * 0.1
great_f0 = f0 * 1000

# Response to sinusoidal signal with frequency 0.1*f0
plot_response("sine", sys, little_f0, t, SINE_RESPONSE_LITTLE_F0_TITLE, 0.501)

# Response to sinusoidal signal with frequency f0
plot_response("sine", sys, f0, t, SINE_RESPONSE_F0_DIAGRAM_TITLE, 0.04)

# Response to sinusoidal signal with frequency 10000*f0
plot_response("sine", sys, great_f0, t, SINE_RESPONSE_GREAT_F0_TITLE, 0.01)

