# cugs_v1

A python-based ground station CLI and GUI software for receiving data via Serial Interface.
This repo includes example CLI and GUI main files and included specifically made library for this type of usages.

## Data Format

Edit file `data_format.txt` in specified `crab` format or in universal `json` format file. Either format are readible and automatically detected.

## Libraries

In `data_handler`:

`lib_preferences_reader.py` manage preferences file with ability to read, write and change format of the preferences file.

`lib_file_class.py` creates and/or loads files, directory and subdirectory for reading, appending, writing, renewing files, or convert `dict` parsed data based on `data_format.txt` data guides.

`lib_gis.py` includes self-explainatory `Coordinate` dataclass and `Gis` class for calculating most GIS values, e.g., Arc Angle, Arc Length, Line of Sight.

`lib_matplotlibchart.py` is for interfacing MATPLOTLIB with PyQt GUI.

`lib_pyqtchart.py` is for interfacing PYQTGRAPH with PyQt GUI.

`lib_parse_data.py` is for parsing data as specified in `data_format.txt`. It includes basic functionality of converting raw delimited string to ordered dictionary of data with its according key, and reducing data `list` set to improve performance when plotting charts.

`lib_mqtt.py` is for usages with MQTT subscribing and publishing topics.

`lib_serial_tools` is for creating a serial manager object and a serial device logger object.

`lib_threading` initializes `QThread` object for working with passed `class`. Signal functionality is also implemented.

`lib_time` create a current-time and delta-time objects.

---
