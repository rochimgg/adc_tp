import sys

import exercices as ex
from constants import ARGV


def main(argv):
    if "1" in sys.argv:
        ex.poles()
        ex.zeros()
        ex.omega_0()
        ex.q()
    if "2a" in sys.argv:
        if len(sys.argv) == 2:
            #ex.bode_mag()
            #ex.bode_phase()
            ex.bode_plot_analytic()
        else:
            if "-mag" in sys.argv:
                ex.bode_mag_analytic()
            elif "-phase" in sys.argv:
                ex.bode_phase_analytic()
    if "2b" in sys.argv:
        ex.step_response_analytic()
    if "2c" in sys.argv:
        ex.impulse_response_analytic()
    if "2d" in sys.argv:
        ex.sine_response_analytic()
    if "2e" in sys.argv:
        ex.square_response_analytic()


if __name__ == "__main__":    # execute only if run as a script
    main(ARGV)
