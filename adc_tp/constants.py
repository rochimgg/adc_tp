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
ARGV = ["1", "2", "5", "6"]

##############
#   Filter   #
##############
gain_a = 0.8911
sys_a = signal.TransferFunction([0.8911, 0, 0, 0, 0], [1, 2539, 4.686e6, 2.894e9, 2.863e12])
t = np.linspace(0, 1, 1000000, endpoint=False)  # time sample
w_a = np.linspace(1, 10000000, 1000000, endpoint=False)  # frequency sample
w_a, mag_a, phase_a = signal.bode(sys_a, w_a)
w0_a = w_a[mag_a < -3][-1]
f0_a = w0_a / (2 * np.pi)

sys_ri = np.polydiv(np.array([-0.27, 0, 0]), np.array([1, 2036.54, 2970885.32]))
sys_ro = np.polydiv(np.array([-3.3, 0, 0]), np.array([1, 263.59, 985027.58]))
sys_r = signal.TransferFunction(np.polymul(np.array([-0.27, 0, 0]), np.array([-3.3, 0, 0])),
                                np.polymul(np.array([1, 2036.54, 2970885.32]), np.array([1, 263.59, 985027.58])))
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
BODE_PLOT_ANALYTIC_DIAGRAM_TITLE = "Diagrama analitico de Bode"
BODE_PLOT_ANALYTIC_DIAGRAM_ZOOM_TITLE = "Diagrama analitico de Bode (zoom)"
BODE_PLOT_REAL_DIAGRAM_TITLE = "Diagrama real de Bode"
BODE_PLOT_REAL_DIAGRAM_ZOOM_TITLE = "Diagrama real de Bode (zoom)"
MAGNITUDE_ANALYTIC_DIAGRAM_TITLE = 'Diagrama de modulo'
IMPULSE_RESPONSE_ANALYTIC_DIAGRAM_TITLE = 'Respuesta analitica a la delta'
PHASE_ANALYTIC_DIAGRAM_TITLE = 'Diagrama de fase'
SINE_RESPONSE_F0_ANALYTIC_DIAGRAM_TITLE = "Respuesta analitica a una señal senoidal de frecuencia $f_0$"
SINE_RESPONSE_GREAT_F0_ANALYTIC_DIAGRAM_TITLE = "Respuesta analitica a una señal senoidal de frecuencia $100\\,f_0$"
SINE_RESPONSE_LITTLE_F0_ANALYTIC_DIAGRAM_TITLE = "Respuesta analitica a una señal senoidal de frecuencia $0.1\\,f_0$"
SQUARE_RESPONSE_F0_ANALYTIC_DIAGRAM_TITLE = "Respuesta analitica a una señal cuadrada de frecuencia $f_0$"
SQUARE_RESPONSE_10_TIMES_F0_ANALYTIC_DIAGRAM_TITLE = "Respuesta analitica a una señal cuadrada de frecuencia $10\\,f_0$"
SQUARE_RESPONSE_F0_OVER_10_ANALYTIC_DIAGRAM_TITLE = "Respuesta analitica a una señal cuadrada de frecuencia $10/f_0$"
STEP_RESPONSE_ANALYTIC_DIAGRAM_TITLE = 'Respuesta analitica al escalon'

SQUARE_RESPONSE_F0_REAL_DIAGRAM_TITLE = "Respuesta real a una señal cuadrada de frecuencia $f_0$"
SQUARE_RESPONSE_10_TIMES_F0_REAL_DIAGRAM_TITLE = "Respuesta real a una señal cuadrada de frecuencia $10\\,f_0$"
SQUARE_RESPONSE_F0_OVER_10_REAL_DIAGRAM_TITLE = "Respuesta real a una señal cuadrada de frecuencia $10/f_0$"
SINE_RESPONSE_F0_REAL_DIAGRAM_TITLE = "Respuesta real a una señal senoidal de frecuencia $f_0$ (real)"
SINE_RESPONSE_GREAT_F0_REAL_DIAGRAM_TITLE = "Respuesta real a una señal senoidal de frecuencia $100\\,f_0$"
SINE_RESPONSE_LITTLE_F0_REAL_DIAGRAM_TITLE = "Respuesta real a una señal senoidal de frecuencia $0.1\\,f_0$"
STEP_RESPONSE_REAL_DIAGRAM_TITLE = 'Respuesta real al escalon'

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
BODE_PLOT_ZOOM_ANALYTIC_FILE_NAME = "bode_plot_zoom_analytic"

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
BODE_PLOT_ZOOM_REAL_FILE_NAME = "bode_plot_zoom_real"

################
#   Messages   #
################
POLES_MESSAGE = "Los polos de la transferencia son: "
ZEROS_MESSAGE = "Los ceros de la transferencia son: "
OMEGA_ZERO_MESSAGE = "La frecuencia natural del circuito es ${\\omega}_0$ = "
QUALITY_FACTOR_MESSAGE = "El factor de calidad es $Q$ = "
