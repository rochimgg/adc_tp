from scipy import signal

##############
#   Filter   #
##############
p = [0.8911, 0, 0, 0, 0]
q = [1, 2539, 4.686e6, 2.894e9, 2.863e12]
sys = signal.TransferFunction(p, q)

##############
# Axis units #
##############

AMPLITUDE_LABEL = 'Amplitud [V]'
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
SQUARE_RESPONSE_F0_DIAGRAM_TITLE = "Respuesta a una señal cuadrada de frecuencia $f_0$"
SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE = "Respuesta a una señal cuadrada de frecuencia $10\\,f_0$"
SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE = "Respuesta a una señal cuadrada de frecuencia $10/f_0$"
SINE_RESPONSE_F0_DIAGRAM_TITLE = "Respuesta a una señal senoidal de frecuencia $f_0$"
SINE_RESPONSE_LITTLE_F0_TITLE = "Respuesta a una señal senoidal de frecuencia $0.1\\,f_0$"
SINE_RESPONSE_GREAT_F0_TITLE = "Respuesta a una señal senoidal de frecuencia $100\\,f_0$"
