def start_prog(mode='cli'):
    if mode == 'cli':
        import cli_ground as gs
        gs.run_prog()
    elif mode == 'gui':
        import gui_ground as gs
    else:
        return 0


if __name__ == '__main__':
    start_prog()