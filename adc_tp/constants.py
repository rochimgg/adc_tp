import numpy as np
from scipy import signal

##############
#   Colors   #
##############
COLOR_SIGNAL_1 = "orange"
COLOR_SIGNAL_2 = "royalblue"

#################
#   Execution   #
#################
ARGV = ["1", "2a", "-mag", "phase", "2b", "2c", "2d", "2e"]

##############
#   Filter   #
##############
sys_a = signal.TransferFunction([0.8911, 0, 0, 0, 0], [1, 2539, 4.686e6, 2.894e9, 2.863e12])
t_a = np.linspace(0, 1, 1000000, endpoint=False)  # time sample
w_a = np.linspace(1, 10000000, 1000000, endpoint=False)  # frequency sample
w_a, mag_a, phase_a = signal.bode(sys_a, w_a)
w0_a = w_a[mag_a < -3][-1]
f0_a = w0_a / (2 * np.pi)

sys_r = signal.TransferFunction([0.8911, 0, 0, 0, 0], [1, 2539, 4.686e6, 2.894e9, 2.863e12])
t_r = np.linspace(0, 1, 1000000, endpoint=False)  # time sample
w_r = np.linspace(1, 10000000, 1000000, endpoint=False)  # frequency sample
w_r, mag_r, phase_r = signal.bode(sys_r, w_r)
w0_r = w_r[mag_r < -3][-1]
f0_r = w0_r / (2 * np.pi)

##############
# Axis units #
##############
AMPLITUDE_LABEL = 'Amplitud $[V]$'
ANGULAR_FREQUENCY_LABEL = 'Frecuencia anglular $\omega$ [rad/s]'
MAGNITUDE_LABEL = 'Modulo [dB]'
PHASE_LABEL = 'Fase [rad]'
TIME_LABEL = 'Tiempo [s]'
OMEGA_LABEL = '$\\omega$ [rad/seg]\\, (log)'

##############
#   Titles   #
##############
BODE_PLOT_DIAGRAM_TITLE = "Diagrama de Bode"
MAGNITUDE_DIAGRAM_TITLE = 'Diagrama de modulo'
IMPULSE_RESPONSE_DIAGRAM_TITLE = 'Respuesta a la delta'
PHASE_DIAGRAM_TITLE = 'Diagrama de fase'
STEP_RESPONSE_DIAGRAM_TITLE = 'Respuesta al escalon'
SQUARE_RESPONSE_F0_DIAGRAM_TITLE = "Respuesta a una señal cuadrada de frecuencia $f_0$"
SQUARE_RESPONSE_10_TIMES_F0_DIAGRAM_TITLE = "Respuesta a una señal cuadrada de frecuencia $10\\,f_0$"
SQUARE_RESPONSE_F0_OVER_10_DIAGRAM_TITLE = "Respuesta a una señal cuadrada de frecuencia $10/f_0$"
SINE_RESPONSE_F0_DIAGRAM_TITLE = "Respuesta a una señal senoidal de frecuencia $f_0$"
SINE_RESPONSE_LITTLE_F0_TITLE = "Respuesta a una señal senoidal de frecuencia $0.1\\,f_0$"
SINE_RESPONSE_GREAT_F0_TITLE = "Respuesta a una señal senoidal de frecuencia $100\\,f_0$"

########################
#   Graphic's Labels   #
########################
IMPULSE_LABEL = "Delta"
SINE_LABEL = "Seno"
SQUARE_LABEL = "Cuadrada"
STEP_LABEL = "Escalón"
RESPONSE_LABEL = "Respuesta"

##################
#   File Names   #
##################
IMPULSE_ANALYTIC_FILE_NAME = "impulse_analytic"
SINE_F0_ANALYTIC_FILE_NAME = "sine_f0_analytic"
SINE_LITTLE_F0_ANALYTIC_FILE_NAME = "sine_little_f0_analytic"
SINE_GREAT_F0_ANALYTIC_FILE_NAME = "sine_great_f0_analytic"
SQUARE_F0_ANALYTIC_FILE_NAME = "square_f0_analytic"
SQUARE_10_TIMES_F0_ANALYTIC_FILE_NAME = "square_10_times_f0_analytic"
SQUARE_F0_OVER_10_ANALYTIC_FILE_NAME = "square_f0_over_10_analytic"
STEP_ANALYTIC_FILE_NAME = "step_analytic"
BODE_MAGNITUDE_ANALYTIC_FILE_NAME = "bode_magnitude_analytic"
BODE_PHASE_ANALYTIC_FILE_NAME = "bode_phase_analytic"
BODE_PLOT_ANALYTIC_FILE_NAME = "bode_plot_analytic"

IMPULSE_REAL_FILE_NAME = "impulse_real"
SINE_F0_REAL_FILE_NAME = "sine_f0_real"
SINE_LITTLE_F0_REAL_FILE_NAME = "sine_little_f0_real"
SINE_GREAT_F0_REAL_FILE_NAME = "sine_great_f0_real"
SQUARE_F0_REAL_FILE_NAME = "square_f0_real"
SQUARE_10_TIMES_F0_REAL_FILE_NAME = "square_10_times_f0_real"
SQUARE_F0_OVER_10_REAL_FILE_NAME = "square_f0_over_10_real"
STEP_REAL_FILE_NAME = "step_real"
BODE_MAGNITUDE_REAL_FILE_NAME = "bode_magnitude_real"
BODE_PHASE_REAL_FILE_NAME = "bode_phase_real"
BODE_PLOT_REAL_FILE_NAME = "bode_plot_real"

################
#   Messages   #
################
POLES_MESSAGE = "Los polos de la transferencia son: "
ZEROS_MESSAGE = "Los ceros de la transferencia son: "
OMEGA_ZERO_MESSAGE = "La frecuencia natural del circuito es ${\\omega}_0$ = "
QUALITY_FACTOR_MESSAGE = "El factor de calidad es $Q$ = "
