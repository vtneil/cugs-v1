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
    else:
        pass


if __name__ == '__main__':
    run(mode='gui')