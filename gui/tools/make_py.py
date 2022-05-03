import os
import sys


def main(argv):
    """
    Use 2 to 3 system arguments: ui file name, py file name and (optional: subfolder name).

    :param argv:
    :return:
    """
    f_dir = "\"" + "\\".join(str(__file__).split("\\")[:-3])
    if len(argv) == 2:
        name_ui, name_py = argv
        subf = "gui"
    elif len(argv) == 3:
        name_ui, name_py, subf = argv
    elif len(argv) == 0:
        name_ui, name_py, subf = "cugs_mainwindow.ui", "cugs_mainwindow.py", "gui"
    else:
        raise ValueError(
            "Generating PySide6 UI must have 2 to 3 arguments: ui file name, py file name and (optional: subfolder name)"
        )
    is_ui = (name_ui[name_ui.rfind("."):] in [".ui", ".UI"])
    is_py = (name_py[name_py.rfind("."):] in [".py", ".PY"])
    if not (is_ui or is_py):
        raise ValueError("(Preliminary Check) UI and PY file extensions don\"t match")
    if not is_ui:
        raise ValueError("(Preliminary Check) UI file extension doesn\"t match")
    if not is_py:
        raise ValueError("(Preliminary Check) PY file extension doesn\"t match")
    py_dir = f_dir + "\{}\{}\"".format(subf, name_py)
    ui_dir = f_dir + "\{}\{}\"".format(subf, name_ui)
    command_os = "pyside6-uic " + ui_dir + " > " + py_dir
    os.system(command_os)
    print('Executed command: \'' + command_os + '\'')
    print('Please check the result accordingly.')
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
