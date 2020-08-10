import sys

import exercices as ex
from constants import ARGV


def main(argv):
    if "1" in sys.argv:
        ex.poles()
        ex.zeros()
        ex.omega_0()
        ex.q()
    if "2a" or "2" in sys.argv:
        if len(sys.argv) == 2:
            #ex.bode_mag()
            #ex.bode_phase()
            ex.bode_plot_analytic()
        else:
            if "-mag" in sys.argv:
                ex.bode_mag_analytic()
            elif "-phase" in sys.argv:
                ex.bode_phase_analytic()
    if "2b" or "2" in sys.argv:
        ex.step_response_analytic()
    if "2c" or "2" in sys.argv:
        ex.impulse_response_analytic()
    if "2d" or "2" in sys.argv:
        ex.sine_response_analytic()
    if "2e" or "2" in sys.argv:
        ex.square_response_analytic()
    if "5a" or "5" in sys.argv:
        ex.bode_plot_real()
    if "5b" or "5" in sys.argv:
        ex.step_response_analytic()
    if "6a" or "6" in sys.argv:
        ex.bode_plot_real()
    if "6b" or "6" in sys.argv:
        ex.step_response_real()
    if "6c" or "6" in sys.argv:
        ex.sine_response_real()
    if "6d" or "6" in sys.argv:
        ex.square_response_real()


if __name__ == "__main__":    # execute only if run as a script
    main(ARGV)
