import sympy as sym
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

p = [0.8911,0,0,0,0]
q = [1, 2539, 4.686e6, 2.894e9, 2.863e12]

sys = signal.TransferFunction(p, q)
w0, mag, phase = signal.bode(sys)

s = sym.symbols('s')
H = (0.8911*s**4)/(s**4+2539*s**3+4.686e6*s**2+2.894e9*s+2.863e12)

##############
# Axis units #
##############

AMPLITUDE_LABEL = 'Amplitud [m]'
ANGULAR_FREQUENCY_LABEL = 'Frecuencia anglular ω [rad/s]'
GAIN_LABEL = 'Modulo [dB]'
PHASE_LABEL = 'Fase [rad]'
TIME_LABEL = 'Tiempo [s]'


##############
#   Titles   #
##############

GAIN_DIAGRAM_TITLE = 'Diagrama de modulo'
IMPULSE_RESPONSE_DIAGRAM_TITLE = 'Respuesta a la delta'
PHASE_DIAGRAM_TITLE = 'Diagrama de fase'
STEP_RESPONSE_DIAGRAM_TITLE = 'Respuesta al escalon'


#################
# Bode Diagrams #
#################

# Gain diagram
plt.figure()
plt.semilogx(w0, mag)
plt.xlabel(ANGULAR_FREQUENCY_LABEL)
plt.ylabel(GAIN_LABEL)
plt.title(GAIN_DIAGRAM_TITLE)
plt.grid()
plt.show()

# Phase diagram
plt.figure()
plt.semilogx(w0, phase)
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

f0 = w0/(2*np.pi)
ten_times_f0 = 10*f0
a_tenth_f0 = f0/10

t = np.linspace(0, 1, 100, endpoint=False) # sampling frequency of 100Hz for my waveforms

# Squared signal with frequency f0
plt.plot(t, signal.square(2 * np.pi * f0 * t))
plt.ylim(-2, 2)

# Squared signal with frequency 10*f0
plt.plot(t, signal.square(2 * np.pi * ten_times_f0 * t))
plt.ylim(-2, 2)

# Squared signal with frequency f0/10
plt.plot(t, signal.square(2 * np.pi * a_tenth_f0 * t))
plt.ylim(-2, 2)


