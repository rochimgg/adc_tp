import ejercicios as ej


def main(argv):
    if argv[1] == "1":
        ej.poles()
        ej.zeros()
        ej.omega_0()
        ej.q()
    if argv[1] == "2a":
        if argv[2] == "-mag":
            ej.bode_mag()
        if argv[2] == "-phase":
            ej.bode_phase()
        else:
            ej.bode_mag()
            ej.bode_phase()
    if argv[1] == "2b":
        ej.step_response()
    if argv[1] == "2c":
        ej.impulse_response()
    if argv[1] == "2d":
        ej.sine_response()
    if argv[1] == "2e":
        ej.square_response()


if __name__ == "__main__":
    # execute only if run as a script
    main("")


