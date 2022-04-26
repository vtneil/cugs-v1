import sys


def run(mode='cli'):
    if mode == 'cli':
        import cli_ground as gs
        gs.run_prog()
    elif mode == 'gui':
        import gui_ground as gs
        gs.run_prog()
    else:
        return 0


def main(argv):
    if len(argv) == 1:
        run(mode=argv[0])
    elif len(argv) == 0:
        run(mode='gui')
    else:
        raise ValueError(
            "Running CUGS must have 0 to 1 argument. "
            "0 argument will run CUGS in GUI mode. "
            "Available arguments are: \"gui\" and \"cli\""
        )


if __name__ == '__main__':
    main(sys.argv[1:])
