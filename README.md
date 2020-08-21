# Geometric Representation of 3-Phase Quantities in a 3D space
Quick and dirty code for animations of 3-phase quantities represented in a 3D space.

Opens a "CSV" file, extracts the data and plots/animates. The "CSV" is actually a TAB-delimited file. The data is organized into columns. The columns have **NO TITLES**.

Programmed on PyCharm Community Edition 2020.1.

Some options are hardcoded as for example showing the balanced 3-phase place, showing the abc bases, etc.

## csv_one3phase.py
Plots/animates a voltage x time chart on the left of all three-phase voltages with a time slider.

Plots/animates a 3D space on the right with the three-phase voltages represented as vectors.

* CSV (tab-delimited) columns: time phaseA phaseB phaseC ...

Other columns in the CSV files will be ignored. 

## csv_two3phase.py
Plots/animates a voltage x time chart on the let of two sets of three-phase voltages with a time slider.

Plots/animates a 3D space on the right with the two sets of three-phase voltages represented as vectors.

* CSV (tab-delimited) columns: time phaseA1 phaseB1 phaseC1 phaseA2 phaseB2 phaseC2 ...

Other columns in the CSV files will be ignored.
