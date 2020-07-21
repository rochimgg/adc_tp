import sys

import exercices as ex


def main():
    if sys.argv[1] == "1":
        ex.poles()
        ex.zeros()
        ex.omega_0()
        ex.q()
    if sys.argv[1] == "2a":
        if len(sys.argv) == 2:
            ex.bode_mag()
            ex.bode_phase()
        else:
            if sys.argv[2] == "-mag":
                ex.bode_mag()
            elif sys.argv[2] == "-phase":
                ex.bode_phase()
    if sys.argv[1] == "2b":
        ex.step_response()
    if sys.argv[1] == "2c":
        ex.impulse_response()
    if sys.argv[1] == "2d":
        ex.sine_response()
    if sys.argv[1] == "2e":
        ex.square_response()


if __name__ == "__main__":    # execute only if run as a script
    main()
