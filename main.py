import sys


def run(mode='cli', pref_file_name=None):
    if mode == 'cli':
        import cli_ground as gs
        if pref_file_name is not None:
            gs.run_prog(pref_file_name)
        else:
            gs.run_prog()
    elif mode == 'gui':
        import gui_ground as gs
        if pref_file_name is not None:
            gs.run_prog(pref_file_name)
        else:
            gs.run_prog()
    else:
        return 0


def main(argv):
    if len(argv) == 0:
        run(mode='gui')
    elif len(argv) == 1:
        run(mode=argv[0])
    elif len(argv) == 2:
        run(mode=argv[0], pref_file_name=argv[1])
    else:
        raise ValueError(
            "Running CUGS must have 0 to 2 argument. "
            "0 argument will run CUGS in GUI mode. "
            "Available arguments are: \"gui\" and \"cli\""
        )


if __name__ == '__main__':
    main(sys.argv[1:])
