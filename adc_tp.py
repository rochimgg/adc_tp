import sys

import ejercicios as ej


def main():
    if sys.argv[1] == "1":
        ej.poles()
        ej.zeros()
        ej.omega_0()
        ej.q()
    if sys.argv[1] == "2a":
        if len(sys.argv) == 2:
            ej.bode_mag()
            ej.bode_phase()
        else:
            if sys.argv[2] == "-mag":
                ej.bode_mag()
            elif sys.argv[2] == "-phase":
                ej.bode_phase()
    if sys.argv[1] == "2b":
        ej.step_response()
    if sys.argv[1] == "2c":
        ej.impulse_response()
    if sys.argv[1] == "2d":
        ej.sine_response()
    if sys.argv[1] == "2e":
        ej.square_response()


if __name__ == "__main__":
    # execute only if run as a script
    main()
